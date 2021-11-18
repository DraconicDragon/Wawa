import time

from discord.ext import commands
import requests


class utils(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unshorten", aliases=["us"])
    async def unshorten(self, ctx, url=None):

        if "http" not in url:
            url = "http://" + url

        try:
            start_time = time.time()
            a = requests.head(url, allow_redirects=True).url
            end_time = time.time()
            time_lapsed = end_time - start_time
            await ctx.send(f"Original URL is: {a} \nThis operation took: {round(time_lapsed, 2)}s")

        except BaseException:
            await ctx.send("Please enter a VALID URL")


def setup(bot):
    bot.add_cog(utils(bot))
