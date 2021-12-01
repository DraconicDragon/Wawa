import json

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Prefix(commands.Cog, name="Administration"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="prefix")
    @has_permissions(administrator=True)
    async def changeprefix(self, ctx, new_prefix=None):
        with open('DBs/prefixDB.json', 'r') as f:
            prefixes = json.load(f)

        old_prefix = prefixes[str(ctx.guild.id)]
        prefixes[str(ctx.guild.id)] = new_prefix

        # if input prefix == set prefix
        if old_prefix == new_prefix:
            embed = discord.Embed(
                title=f"The prefix is already `{old_prefix}`",
                color=0x3389e6
            )
            await ctx.send(embed=embed)

        # if input is not provided
        elif new_prefix is None:
            embed = discord.Embed(
                title=f"The current prefix is: `{old_prefix}`",
                color=0x3389e6
            )
            await ctx.send(embed=embed)

        # if input successfully set as new prefix
        else:
            with open('DBs/prefixDB.json', 'w') as f:
                json.dump(prefixes, f, indent=4)
            embed = discord.Embed(
                title=f'Prefix changed from `{old_prefix}` to: `{new_prefix}`',
                color=0x31d88e
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Prefix(bot))
