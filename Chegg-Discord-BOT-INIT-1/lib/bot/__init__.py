from discord.ext.commands import Bot as BotBase
from glob import glob
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Context
from ..db import db
from apscheduler.triggers.cron import CronTrigger
from asyncio import sleep
import os
import discord
from lib.bot.cheggapi import getLink
from lib.bot.firebaseauth import addUser, getUser, getUserMail, updateMail, deleteUser, addQuestion, updateQuestion, \
    getQuestion, deleteQuestion, fetchAllUsers
from lib.bot.saveMail import findQuestionId
from lib.bot.log import Log

PREFIX = "+"
OWNER_IDS = [618038532665114624]
COGS = [path.split(os.sep)[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f"{cog} is Ready!")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        self.log = Log(r"C:\Users\woosal\Desktop\Chegg BOT X", "chegg.log")

        db.autosave(self.scheduler)
        super().__init__(command_prefix=PREFIX, OWNER_IDS=OWNER_IDS)

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def setup(self):
        for cog in COGS:
            print(cog)
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} was loaded!")

        print("Setup Completed!")

    def run(self, version):
        self.VERSION = version

        print("Running Setup...")
        self.log.info("INIT_1:Setup")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running bot...")
        self.log.info("INIT_1:Run")
        super().run(self.TOKEN, reconnect=True)

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=Context)

        if ctx.command is not None and ctx.guild is not None:
            if self.ready:
                await self.invoke(ctx)

            else:
                await ctx.send("I'm not listening to your commands you psycho, maybe later...")

    async def print_message(self):
        await self.stdout.send("Good Morning!")

    async def on_connect(self):
        print("BOT has been CONNECTED!")
        self.log.info("INIT_1:Connected")

    async def on_disconnect(self):
        print("BOT has been DISCONNECTED!")
        self.log.alert("INIT_1:Disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            self.log.alert("INIT_1:on_command_error")
        else:
            channel = self.stdout
            self.log.alert(f"INIT_1:{err}:{channel}")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            return 1

        elif hasattr(exc, "original"):
            pass
        else:
            raise exc

    async def on_ready(self):

        if not self.ready:
            self.channel = self.get_channel(801895525263343656)
            self.ready = True
            self.cogs_ready = Ready()
            self.guild = self.get_guild(801895525263343656)
            self.stdout = self.get_channel(801895525263343656)
            self.scheduler.add_job(self.print_message, CronTrigger(day_of_week=0, hour=12, minute=0, second=0))
            self.scheduler.start()

            await bot.change_presence(activity=discord.Game(name="https://github.com/Chegg-BOT"))


            while self.cogs_ready.all_ready():
                await sleep(0.5)


        else:
            self.log.info("INIT_1:Reconnect")
            print("BOT reconnected!")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)


bot = Bot()
