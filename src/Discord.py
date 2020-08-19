import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from Cogs.Music import Music
from Cogs.Misc import Misc

from Utils.Logger import Logger
from Utils.Secrets import PREFIX, TOKEN, TOKEN_DEV

from Database.DBUtils import isUserBlocked

from discord.abc import PrivateChannel
import asyncio

from Support.Support import supportHandler, supportResponder

bot = commands.Bot(command_prefix="!", case_insensitive=True)

logger = Logger(True)
dev = True


@bot.event
async def on_ready():
    logger.success("Discord", "Connected to gateway!")
    bot.add_cog(Music(bot))
    bot.add_cog(Misc(bot))
    bot.load_extension('Cogs.Developer')
    bot.load_extension('Cogs.Support')
    
@bot.event
async def on_message(message):
    response = ""
    if message.author.id == bot.user.id: return
    if isUserBlocked(message.author.id) == True: return

    chan = isinstance(message.channel, PrivateChannel)
    if chan == True:
        await supportHandler(message, bot)

    if message.guild.id == 669092504121114644:
        if "ticket-" in message.channel.name:
            num = str(message.channel.name)
            num = num.replace("ticket-", "")
            await supportResponder(num, message, bot)
    
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return logger.warning("Discord", f"{ctx.author.name} invoked an unkown command.")
    logger.error("Discord", f"Command Error: {error}")
    raise error
    

if __name__ == "__main__":
    if dev: bot.run(TOKEN_DEV)
    else: bot.run(TOKEN)
