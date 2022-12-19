import discord
from discord.ext import commands, tasks
from config import TOKEN
from config import PREFIX
import os
from itertools import cycle 

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

bot_status = cycle(["Status 1", "Status 2", "Status 3", "Status 4", "Status 5"])

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))


@bot.event
async def on_ready():
    print("✅ | Successfully connected to discord!")
    change_status.start()


for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")


bot.run(TOKEN)
