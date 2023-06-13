import os
import nextcord
from nextcord.ext import commands
from nextcord import File

from config import DISCORD_TOKEN, COMMAND_PREFIX, DISCORD_SERVER_TOKEN


intents = nextcord.Intents.default()
intents.message_content = True
# intents.members = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


@bot.event
async def on_ready():
    target_guild = bot.get_guild(DISCORD_SERVER_TOKEN)

    if target_guild:
        await bot.change_presence(
            status=nextcord.Status.online,
            activity=nextcord.Activity(
                type=nextcord.ActivityType.listening,
                name="your destiny",
            ),
        )
        print("Destiny is On!")
    else:
        print("Bot is not a member of the target guild.")


# loading cogs
initial_extension = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extension.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extension:
        bot.load_extension(extension)


bot.run(DISCORD_TOKEN)
