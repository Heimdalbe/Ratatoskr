# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class HeimdalClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member):
            print(f'Member with name {member.name} has joined')
            await member.create_dm()
            await member.dm_channel.send(
                f'WILKOMMEN {member.name}, TO ZE GREATEST SERVER IN ZE HISTORY OF SERVERS!'
            )

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content.startswith('!socials'):
            await message.channel.send(
                f'Website: https://heimdal.be \n'
                f'Facebook: https://www.facebook.com/Heimdal.be/ \n'
                f'Instagram: https://www.instagram.com/heimdalgent/ \n'
                f'Youtube: https://www.youtube.com/channel/UCW8aHQcjgUXo33nqnZgd3hg'
            )
    

bot = HeimdalClient()


bot.run(TOKEN)