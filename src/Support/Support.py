import random as r

import discord
from discord.utils import get

from Utils.Cache import support_tickets_cache, ticket_numbers, support_nums_id_cache
from Utils.Secrets import COLOUR

def isMe(ctx):
    return ctx.author.id == bot.user.id


def getSupportNumber():
    while 1:
        num = r.randint(1000, 9999)
        if num not in ticket_numbers:
            ticket_numbers.append(num)
            return num
            break
        

async def supportHandler(ctx, bot):
    if str(ctx.author.id) not in support_tickets_cache:
        await ctx.channel.send("Would you like to create a ticket? (yes/no)")
        
        response = await bot.wait_for('message', check=lambda message: message.author.id == ctx.author.id)
        
        if response.content.lower() in ['yes', 'y']:
            num = getSupportNumber()
            og_msg = ctx.content
            support_tickets_cache[f"{ctx.author.id}"] = f"{num}"
            support_nums_id_cache[f"{num}"] = str(ctx.author.id)
            await ctx.channel.send(f"Ticket created! #{support_tickets_cache[str(ctx.author.id)]}")

            #reqChan = bot.get_channel(744069415468793906)
            em = discord.Embed()
            em.colour = COLOUR
            em.title = f"Support Request: #{num}"
            em.description = f"**Query**: {og_msg}\n\n**Name**: {ctx.author}\n**ID**: {ctx.author.id}"
            
            myGuild = bot.get_guild(669092504121114644)
            await myGuild.create_text_channel(name=f"ticket-{num}", category=bot.get_channel(744118420144128032))

            channel = get(myGuild.channels, name=f"ticket-{support_tickets_cache[str(ctx.author.id)]}", type=discord.ChannelType.text)
            
            await bot.get_channel(channel.id).send("@everyone")
            await bot.get_channel(channel.id).send(embed=em)
            #await bot.get_channel(channel.id).send(f"**{ctx.author}**: {ctx.content}")

            return
        else:
            support_tickets_cache[str(ctx.author.id)] = "NULL"
            await ctx.channel.send(f"Ticket Creation Cancelled")
            support_tickets_cache.pop(str(ctx.author.id))
            return

    
    if str(ctx.author.id) in support_tickets_cache:
        myGuild = bot.get_guild(669092504121114644)
        channel = get(myGuild.channels, name=f"ticket-{support_tickets_cache[str(ctx.author.id)]}", type=discord.ChannelType.text)
        await bot.get_channel(channel.id).send(f"**{ctx.author}**: {ctx.content}")

async def supportResponder(num, ctx, bot):
    user_id = int(support_nums_id_cache[num])
    await bot.get_user(user_id).send(f"**(Support) {ctx.author}**: {ctx.content}")