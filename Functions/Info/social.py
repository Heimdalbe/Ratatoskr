import random
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

import bot

guild_ids = [714472652584255488]
whatIsHeimdal = ["Geen drankvereniging", "Geen pestvereniging", "Geen anti-drankvereniging"]

class InfoCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="socials", guild_ids=guild_ids,
                       description="All the Heimdal socials you could possibly need")
    async def socials(self, ctx: SlashContext):
        await ctx.send(
            f'Website: https://heimdal.be \n'
            f'Facebook: https://www.facebook.com/Heimdal.be/ \n'
            f'Instagram: https://www.instagram.com/heimdalgent/ \n'
            f'Youtube: https://www.youtube.com/channel/UCW8aHQcjgUXo33nqnZgd3hg'
        )

    @cog_ext.cog_slash(name="heimdal", guild_ids=guild_ids, description="Vind nu uit wat Heimdal nu eigenlijk is")
    async def whatIs(self, ctx: SlashContext):
        await ctx.send(
            f'{random.choice(whatIsHeimdal)}'
        )

    @cog_ext.cog_slash(name="fwb", guild_ids=guild_ids, description="???")
    async def whatIs(self, ctx: SlashContext):
        await ctx.send(
            f'We are the friends with Blankets'
        )


def setup(bot: Bot):
    bot.add_cog(InfoCog(bot))