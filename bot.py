# bot.py
import os
import settings
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

cogs_list = [
    'cogs.info.social',
    'cogs.info.help',
    'cogs.admin.clear',
]

intents = discord.Intents.all()
bot = discord.Bot(debug_guilds=[714472652584255488], intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    game = discord.Game('never gonna give you up')
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.event
async def on_message(message):
    print(message.content)
    # Make sure the bot doesn't react to itself
    if message.author == bot.user:
        return
    if message.author.bot: return
    if 'stamboom' in message.content.lower():
        await message.channel.send('De StAmBoOm Is GeEn PrIoRiTeIt!')


for cog in cogs_list:
    bot.load_extension(f'{cog}')
    print(f'loaded {cog}')

bot.run(TOKEN)  # run the bot with the token
