import discord
from discord.ext import commands

guild_ids = [714472652584255488]


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='help', description='An overview of all commands available to you',
                           guild_ids=guild_ids)
    async def help(self, ctx):
        await ctx.defer()
        await ctx.followup.send(
            f'/socials: toon alle social media van Heimdal \n'
            f'/heimdal: ontdek wat Heimdal nu eigenlijk is \n'
            f'/fwb: ???'
        )


def setup(bot):
    bot.add_cog(Help(bot))
