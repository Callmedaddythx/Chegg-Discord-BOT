import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from lib.bot.cheggapi import getLink
from lib.bot.firebaseauth import addUser, getUser, getUserMail, updateMail, deleteUser
from datetime import datetime


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="addmail", aliases=["adduser"])
    async def add_mail(self, ctx, mail):
        #############################################
        newUser = [str(ctx.message.author.id), mail]

        print("New User: ", newUser)
        newUserRes = getUser(newUser[0])
        # User already registered
        if newUserRes != None:
            newUserResMail = getUserMail(newUser[0])
            print("Such user already registered with the mail of {0}".format(newUserResMail))
            await ctx.author.send("Such user already registered with the mail of {0}".format(newUserResMail))
            print("\n")

            return True

        # User is registering for the first time
        else:
            print(addUser(newUser[0], newUser[1]))
            print("Mail has been added successfully!")
            await ctx.author.send("Your mail has been successfully added!")
            print("\n")

            return True
        #############################################

    @command(name="commands", aliases=["info", "about"])
    async def help(self, ctx):
        embed = discord.Embed(title="Chegg BOT", url="https://cheggbot.woosal.com/",
                              description="Unblur the answers of the Chegg questions, and get receive them.",
                              color=0xfbc041)
        embed.set_author(name="woosal", url="https://woosal.com/",
                         icon_url="https://woosal.com/1337/woosal1337-AxcOjfpPCjYo2aMU9s05XvXnLk3SGXC67oJq7CZ6d0TCTRPzMKZ8D9q5g7W4fIdWwmwRVQHdYvffkr16RsEdD0Y1Y.png")
        embed.set_thumbnail(url="https://woosal.com/1337/cheggwpfullblacklogoleftnobg.png")
        embed.add_field(name="Add Your Email", value="+addmail your@mail.com", inline=False)
        embed.add_field(name="Search For The Question", value="+chegg URL", inline=False)
        embed.add_field(name="Commands", value="+commands", inline=False)
        embed.add_field(name="Your Current Mail Info", value="+mymail", inline=False)
        embed.add_field(name="Update Your Mail to New Mail", value="+updatemail newmail@mail.com", inline=False)
        embed.add_field(name="Delete Your Mail Completely", value="+deletmail", inline=False)
        embed.add_field(name="Want a new feature?", value="chegg@woosal.com", inline=False)
        embed.set_footer(text="Star the project on GitHub: https://github.com/woosal1337/Chegg-Discord-BOT")
        await ctx.send(embed=embed)
        return True

    @command(name="chegg", aliases=["check", "cheggapi", "search"])
    async def chegg_answer(self, ctx, link):

        userid = str(ctx.message.author.id)

        newUserRes = getUser(userid)

        if newUserRes != None:
            if "chegg.com" in link:
                newUserResMail = newUserRes["mail"]

                await ctx.author.send("I am searching for the answer, please give me a few seconds!")
                print("User: {0}; Link:{1}".format(ctx.message.author, link))
                print(getLink(newUserResMail, str(link)))
                await ctx.author.send(
                    "Dear {1}, I am sending the answer to {0}, you will get it in a few minutes!".format(newUserResMail, ctx.message.author))

                return True

            else:
                await ctx.author.send("Dear {0}, Please use only official Chegg links, this link is not recognized!".format(ctx.message.author))
                print("Wrong link was used: {0}".format(link))
                return True

        else:
            await ctx.author.send(
                "You have not added your email to our database, make sure to add your own email by using```+addmail YOUREMAIL@mail.com```")
            print("This user has not registered a mail to our database yet.")
            return True

    @command(name="updatemail", aliases=["newmail", "mainmail", "changemail"])
    async def update_mail(self, ctx, mail):
        # +updatemail woosal@protonmail.com 1

        userid = str(ctx.message.author.id)

        if getUser(userid) != None:
            await ctx.author.send("Your email has been updated to {0}".format(mail))
            print(updateMail(userid, mail))
            return True
        else:
            await ctx.author.send(
                "This user has not registered any mails yet, please use ```+addmail yourmail@mail.com``` to create your account!")
            print(
                "This user has not registered any mails yet, please use ```+addmail yourmail@mail.com``` to create your account!")
            return True

    @command(name="mymail", aliases=["currentmail", "mycurrentmail", "savedmail", "mysavedmail", "mail"])
    async def current_mail(self, ctx):

        userid = str(ctx.message.author.id)

        if getUser(userid) != None:
            await ctx.author.send(
                "Your current saved mail to your Discord account is ```{0}``` You can update it anytime you want by using ```+updatemail newmail@mail.com```".format(getUserMail(userid)))
            print("Your current saved mail to your Discord account is ```{0}``` You can update it anytime you want by using ```+updatemail newmail@mail.com```".format(getUserMail(userid)))
            return True
        else:
            await ctx.author.send("This user has not registered any mails yet, please use ```+addmail yourmail@mail.com``` to create your account")
            print("This user has not registered any mails yet, please use ```+addmail yourmail@mail.com``` to create your account")
            return True

    @command(name="deletemail", aliases = ["purgemail", "delete", "removemail", "removeme", "purgeme"])
    async def delete_user(self, ctx):

        print("Delete user request was received.")
        userid = str(ctx.message.author.id)

        if getUser(userid) != None:
            print(deleteUser(userid))

            await ctx.author.send("Dear {0}, your mail was removed!".format(ctx.message.author))
            print("Dear {0}, your mail was removed!".format(ctx.message.author))

            return True

        else:
            await ctx.author.send("Dear {0}, your have not even registered yet, please consider registering at first by using the command: ```+addmail yourmail@mail.com```".format(ctx.message.author))
            print("Dear {0}, your have not even registered yet, please consider registering at first by using the command: ```+addmail yourmail@mail.com```".format(ctx.message.author))

            return True

@Cog.listener()
async def on_ready(self):
    if not self.bot.ready:
        self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
