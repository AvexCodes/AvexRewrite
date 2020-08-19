from twitchio.ext import commands
from Utils.Logger import Logger
from Utils.Secrets import IRC_TOKEN, NICK, CLIENT_ID, PREFIX, INITIAL_CHANNELS

bot = commands.Bot(irc_token=IRC_TOKEN,
                   nick=NICK,
                   client_id=CLIENT_ID,
                   prefix=PREFIX,
                   initial_channels=INITIAL_CHANNELS)
modules = ["Modules.Misc"]

logger = Logger(True)

@bot.event
async def event_ready():
    logger.success(name="Twitch", output="Connected to gateway!")
    for i in modules:
        try:
            bot.load_module(i)
        except Exception as e:
            logger.error(name="Twitch", output=f"Error loading {i}. {e}")

if __name__ == "__main__":
    bot.run()