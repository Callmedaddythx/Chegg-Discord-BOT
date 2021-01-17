import csv
from discord.ext.commands import Cog
from discord.ext.commands import command

filename = r"D:\GitHub\Chegg-Discord-BOT\lib\cogs\mails.csv"


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="addmail", aliases=["adduser"])
    async def add_mail(self, ctx, mail):
        newUser = [str(ctx.message.author.id), mail]

        print(newUser)

        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            for line in csvreader:
                if line[0] == newUser[0]:
                    print("Such user already registered with the mail of {0}".format(line[1]))
                    await ctx.send("Such user already registered with the mail of {0}".format(line[1]))
                    return True

            with open(filename, 'a+', newline='') as writecsv:
                csvwriter = csv.writer(writecsv)
                csvwriter.writerow(newUser)
                print("Function is done.")
                await ctx.send("New user has been added!")
                return True




# Reply Hello/Hi/Hey/Hiya to the given hello command
# @command(name="hello", aliases=["hi"])
# async def say_hello(self, ctx):
#     await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention} !")


# Roll a dice and print it
# @command(name="dice", aliases=["roll"])
# async def roll_dice(self, ctx, die_string: str):
#     dice, value = (int(term) for term in die_string.split("d"))
#     rolls = [randint(1, value) for i in range(dice)]
#
#     await ctx.send(" + ".join([str(r) for r in rolls]) + f" = {sum(rolls)}")


# Send a file using the bot command
# @command(name="slap", aliases=["hit"])
# async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "no reason"):
#     await ctx.send(f"{ctx.author.mention} slapped {member.mention}  {reason}!")
#     await ctx.send(file=File("./data/images/slap.gif"))


# Rsend the same message using the bot and delete your last message
# @command(name="echo", aliases=["say"])
# async def echo_message(self, ctx, *, message):
#     await ctx.message.delete()
#     await ctx.send(message)

@Cog.listener()
async def on_ready(self):
    if not self.bot.ready:
        self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
