import csv
import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from lib.bot.cheggcheck import QuestionBot
from lib.bot.cheggapi import getLink
from firebase import firebase
from lib.bot.firebaseauth import addUser, getUser, getUserMail
from datetime import datetime

firebase = firebase.FirebaseApplication('', None)


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="addmail", aliases=["adduser"])
    async def add_mail(self, ctx, mail):
        timeStart = datetime.now()

        #############################################
        newUser = [str(ctx.message.author.id), mail]

        print("New User: ", newUser)
        newUserRes = getUser(newUser[0])
        # User already registered
        if newUserRes != None:
            newUserResMail = getUserMail(newUser[0])
            print("Such user already registered with the mail of {0}".format(newUserResMail))
            await ctx.send("Such user already registered with the mail of {0}".format(newUserResMail))
            print("\n")

            timeEnd = datetime.now()
            print("Total time it took: {0}".format(timeEnd - timeStart))
            return True

        # User is registering for the first time
        else:
            print(addUser(newUser[0], newUser[1]))
            print("Mail has been added successfully!")
            await ctx.send("Your mail has been successfully added!")
            print("\n")

            timeEnd = datetime.now()
            print("Total time it took: {0}".format(timeEnd - timeStart))
            return True
        #############################################

    @command(name="commands", aliases=["info", "about"])
    async def help(self, ctx):
        embed = discord.Embed(title="Chegg BOT", url="https://cheggbot.woosal.com/",
                              description="Unblur the answer of the Chegg questions, and get receive them.",
                              color=0xfbc041)
        embed.set_author(name="woosal", url="https://woosal.com/",
                         icon_url="https://woosal.com/1337/woosal1337-AxcOjfpPCjYo2aMU9s05XvXnLk3SGXC67oJq7CZ6d0TCTRPzMKZ8D9q5g7W4fIdWwmwRVQHdYvffkr16RsEdD0Y1Y.png")
        embed.set_thumbnail(url="https://woosal.com/1337/cheggwpfullblacklogoleftnobg.png")
        embed.add_field(name="Add Your Email", value="+addmail your@mail.com", inline=False)
        embed.add_field(name="Search For The Question", value="+chegg URL", inline=False)
        embed.add_field(name="Commands", value="+commands", inline=False)
        embed.add_field(name="Want a new feature?", value="chegg@woosal.com", inline=False)
        embed.set_footer(text="Star the project in GitHub: https://github.com/woosal1337/Chegg-Discord-BOT")
        await ctx.send(embed=embed)
        return True

    @command(name="chegg", aliases=["check", "cheggapi", "search"])
    async def chegg_answer(self, ctx, link):

        userid = str(ctx.message.author.id)

        newUserRes = getUser(userid)

        if newUserRes != None:
            newUserResMail = newUserRes["mail"]

            await ctx.send("I am searching for the answer, please give me a few seconds!")
            print("User: {0}; Link:{1}".format(ctx.message.author, link))
            print(getLink(newUserResMail, str(link)))
            await ctx.send(
                "I am sending the answer to {0}, you will get it in a few minutes!".format(newUserResMail))

            return True

        else:
            await ctx.send(
                "You have not added your email to our database, make sure to add your own email by using```+addmail YOUREMAIL@mail.com```")
            print("This user has not registered a mail to our database yet.")
            return True


# Send a file using the bot command
# @command(name="slap", aliases=["hit"])
# async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "no reason"):
#     await ctx.send(f"{ctx.author.mention} slapped {member.mention}  {reason}!")
#     await ctx.send(file=File("./data/images/slap.gif"))

@Cog.listener()
async def on_ready(self):
    if not self.bot.ready:
        self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
