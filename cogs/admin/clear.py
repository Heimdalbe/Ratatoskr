import discord
from discord.ext import commands
from discord.commands import Option

guild_ids = [714472652584255488]


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Add check on user permissions based on role/permission
    @discord.slash_command(name="clear", description="Verwijder x aantal berichten in de chat",
                           guild_ids=guild_ids)
    # @commands.has_role('Admin')
    async def clear(self, ctx, aantal: Option(int, "Het aantal te verwijderen berichten", required=True)):
        await ctx.defer()
        async for message in ctx.channel.history(limit=aantal+1):
            await message.delete()


def setup(bot):
    bot.add_cog(Clear(bot))
