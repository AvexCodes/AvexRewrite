import discord
from discord.ext import commands    

from Database.DBUtils import isUserDeveloper, updateUser

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def DeveloperOnly():
        async def predicate(ctx):
            if isUserDeveloper(str(ctx.author.id)) == True: return True
            else: 
                await ctx.send("Sorry, but this command is `DEVELOPER` only!")
                return False
        return commands.check(predicate)
        
    @DeveloperOnly()
    @commands.command(name="giverank", aliases=['gr'])
    async def _giverank(self, ctx, member: discord.User = None, tier: int = 1):
        """
            Give's the specified user a rank.
        """
        if member is None:
            return await ctx.send('Idiot, specify a user.')
        if member.id == ctx.author.id:
            return await ctx.send("You can't change your own rank!")
        
        updateUser(str(member.id), tier)
        await ctx.send(f"Updating {member} tier to {tier}!")

    
def setup(bot):
    bot.add_cog(Developer(bot))