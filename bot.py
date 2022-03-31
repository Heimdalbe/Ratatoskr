# bot.py
import os

import discord
from discord import Intents
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord_slash import SlashCommand

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


"""class HeimdalClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member):
            print(f'Member with name {member.name} has joined')
            await member.create_dm()
            await member.dm_channel.send(
                f'WILKOMMEN {member.name}, TO ZE GREATEST SERVER IN ZE HISTORY OF SERVERS!'
            )

bot = HeimdalClient()"""

bot = Bot(command_prefix="!", self_bot=True, help_command=None, intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Connected to discord")

bot.load_extension("social")
bot.run(TOKEN)
