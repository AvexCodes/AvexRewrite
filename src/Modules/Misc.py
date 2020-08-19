from twitchio.ext import commands
import random as r
@commands.cog()
class Misc():
    def __init__(self, bot):
        self.bot = bot
        print('Misc Cog Loaded!')

    @commands.command(name="ping")
    async def _ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command(name="gay")
    async def _gay(self, ctx):
        await ctx.send(f"{ctx.author.name} is {r.randint(0, 100)}% gay!")