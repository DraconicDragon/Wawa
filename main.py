import os
from discord.ext.commands import Bot
from cogs.Listeners import prefix_manager

bot = Bot(
    case_insensitive=True,
    command_prefix=prefix_manager.get_prefix,
)


@bot.event
async def on_ready():
    print("-----------------------\nLogged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)

    if message.content.startswith('wawa reload'):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    bot.reload_extension(f"cogs.{extension}")
                    print(f"reloaded '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    print(f"Error occurred for {extension}:\n{exception}")


def cogs_dir(dir, ext_dir):
    for file in os.listdir(f"{dir}"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"{ext_dir}.{extension}")
                print(f"loaded '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Error occurred for {extension}:\n{exception}")

cogs_dir("cogs", "cogs")
cogs_dir("cogs/Listeners", "cogs.Listeners")


bot.run('TOKEN')
