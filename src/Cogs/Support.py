import discord
from discord.ext import commands
from discord.utils import get

from Utils.Logger import Logger
from Database.DBUtils import isUserSupport

from Utils.Cache import support_nums_id_cache, support_tickets_cache

class Support(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        #self.logger = Logger(False)
    
    def SupportOnly():
        async def predicate(ctx):
            if isUserSupport(ctx.author.id) == True: return True
            else:
                await ctx.send(f"Sorry but this command is restricted to `SUPPORT` or higher!")
                return False
        return commands.check(predicate)

    @SupportOnly()
    @commands.command(name="close")
    async def _close(self, ctx, num: int=None, *, reason = None):
        """
            Close a support ticket
        """
        if num is None:
            return await ctx.send(f"Probably helps if you specified a support number!")

        if reason is None: reason = "Resolved"
        id = support_nums_id_cache[str(num)]
        support_nums_id_cache.pop(str(num))
        support_tickets_cache.pop(str(id))

        myGuild = self.bot.get_guild(669092504121114644)
        channel = get(myGuild.channels, name=f"ticket-{num}", type=discord.ChannelType.text)
        await self.bot.get_channel(channel.id).delete(reason=reason)
        
        await self.bot.get_user(int(id)).send(f"Ticket #{num} has been closed, for the reason: {reason}")
        await ctx.message.add_reaction('☑️')


def setup(bot):
    bot.add_cog(Support(bot))


