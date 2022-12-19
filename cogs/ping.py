import discord
from discord.ext import commands
from main import bot

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(bot.latency * 1000)
        await ctx.send(f"Pong! Latency: {bot_latency}ms")

def setup(bot):
    bot.add_cog(General(bot))