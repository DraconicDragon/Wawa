import json

from discord.ext import commands
from discord.ext.commands import when_mentioned_or

class prefix_event_listener(commands.Cog, name="prefix manager"):
    def __init__(self, bot):
        self.bot = bot

    # when the bot joins a guild it will add a default prefix to the guild
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
            with open('DBs/prefixDB.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(guild.id)] = '-'
            with open('DBs/prefixDB.json', 'w') as f:
                json.dump(prefixes, f, indent=4)

    # when the bot leaves a guild it will remove any prefix that has been set for that guild
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
            with open('DBs/prefixDB.json', 'r') as f:
                prefixes = json.load(f)

            prefixes.pop(str(guild.id))

            with open('DBs/prefixDB.json', 'w') as f:
                json.dump(prefixes, f, indent=4)

def setup(bot):
    bot.add_cog(prefix_event_listener(bot))


def get_prefix(bot, msg):
    with open('DBs/prefixDB.json', 'r') as file:
        prefixes = json.load(file)
    prefix = prefixes[str(msg.guild.id)]
    return when_mentioned_or(prefix)(bot,msg)
