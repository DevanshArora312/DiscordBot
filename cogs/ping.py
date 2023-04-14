import discord 
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await print("Cog ready")

    @commands.command()
    async def ping(self,ctx):
        bot_latency = round(1000* self.bot.latency)
        await ctx.send(f"Pong {bot_latency}ms")

async def setup(bot):
    await bot.add_cog(Ping(bot))