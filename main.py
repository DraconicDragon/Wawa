import os
from discord.ext.commands import Bot
from cogs.Listeners import prefix_manager

bot = Bot(
    case_insensitive=True,  # don't ask me.
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


# loading cogs
def load_cogs():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"loaded '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Error occurred for {extension}:\n{exception}")

    # same thing for cogs/Listeners
    for file in os.listdir("cogs/Listeners"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.Listeners.{extension}")
                print(f"loaded '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Error occurred for {extension}:\n{exception}")


load_cogs()

bot.run('TOKEN')
