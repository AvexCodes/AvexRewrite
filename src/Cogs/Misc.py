import discord
from discord.ext import commands

from Utils.Logger import Logger
from Database.Database import DatabaseHandler

from Database.DBUtils import getUserTier, isUserDeveloper

from Utils import Cache
from Utils.Secrets import COLOUR

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = Logger(False)
        self.logger.log(name="Discord", output="Misc Cog Loaded!")
        self.db = DatabaseHandler(db="database.db")
        self.db.connect()
    
    @commands.command(name="ping", aliases=["pang", "peng", "pong", "pung"])
    async def _ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        e = discord.Embed()
        if ping < 30:
            e.colour = 0x39fc03
        elif ping < 75:
            e.colour = 0xf7ba00
        else:
            e.colour = 0xf70000
        
        e.title = "Pong! :ping_pong:"
        e.description = f"API Latency: {ping}ms"

        await ctx.send(embed=e)
    @commands.command(name="tier", aliases=["rank"])
    async def _tier(self, ctx, member: discord.User = None):
        tier = ""
        em = discord.Embed()
        em.colour = COLOUR
        if member is None:
            # do invoker
            em.title = f"{ctx.author.name}'s Tier"
            tier = getUserTier(ctx.author.id)
            em.description = f"Your current tier is: {tier}!"
            return await ctx.send(embed=em)

        em.title = f"{member.name}'s Tier"
        tier = getUserTier(member.id)
        em.description = f"{member.name} tier is: {tier}!"
        await ctx.send(embed=em)

    @commands.command(name="test")
    async def _test(self, ctx):
        await ctx.send(isUserDeveloper(ctx.author.id))
        
        
def setup(bot):
    bot.add_cog(Misc(bot))
