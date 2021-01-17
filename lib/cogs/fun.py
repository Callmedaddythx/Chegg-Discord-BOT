import csv
from discord.ext.commands import Cog
from discord.ext.commands import command
from lib.bot.cheggcheck import QuestionBot

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

    @command(name="chegg", aliases=["check"])
    async def chegg_answer(self, ctx, link):

        userId = str(ctx.message.author.id)

        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            for line in csvreader:
                if line[0] == userId:
                    userMail = line[1]

                    await ctx.send("I am searching for the answer, please give me a few seconds!".format(userMail))
                    bot = QuestionBot(r"C:\firefoxdriver\geckodriver.exe", str(ctx.message.author), userMail)
                    bot.main(str(link))
                    await ctx.send("I have sent the answer to {0}, makes sure to check it within a few minutes!".format(userMail))

                    return True

            await ctx.send("You have not added your email to our database, make sure to add your own email by using```+addmail YOUREMAIL@mail.com```")
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
