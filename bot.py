# bot.py
import os
import settings
import discord
from discord import Intents
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord_slash import SlashCommand

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

cogs: list = ["Functions.Info.social"]

bot = Bot(command_prefix=settings.Prefix, self_bot=True, help_command=None, intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Connected to discord")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            bot.load_extension(cog)
            print(f"Loaded cog {cog}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))

bot.run(TOKEN)
