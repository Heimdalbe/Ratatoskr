import random
import discord
from discord.ext import commands

whatIsHeimdal = ["geen drankvereniging", "geen pestvereniging", "geen anti-drankvereniging"]
guild_ids = [714472652584255488]


class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="socials", description="All the Heimdal socials you could possibly need",
                           guild_ids=[714472652584255488])
    async def socials(self, ctx):
        await ctx.defer()
        await ctx.followup.send(
            f'Website: https://heimdal.be \n'
            f'Facebook: https://www.facebook.com/Heimdal.be/ \n'
            f'Instagram: https://www.instagram.com/heimdalgent/ \n'
            f'Youtube: https://www.youtube.com/channel/UCW8aHQcjgUXo33nqnZgd3hg'
        )

    @discord.slash_command(name="heimdal", guild_ids=[714472652584255488],
                           description="Vind uit wat Heimdal nu eigenlijk is")
    async def whatis(self, ctx):
        await ctx.defer()
        await ctx.followup.send(
            f'Heimdal is {random.choice(whatIsHeimdal)}'
        )

    @discord.slash_command(name="fwb", guild_ids=[714472652584255488], description="???")
    async def friendswithblankets(self, ctx):
        await ctx.defer()
        await ctx.followup.send(
            f'We are the friends with Blankets'
        )


def setup(bot):
    bot.add_cog(Social(bot))
