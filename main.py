import discord
from discord.ext import commands
import os
import asyncio

from dotenv import load_dotenv
load_dotenv() 

token_key = os.getenv('TOKEN')

TOKEN = token_key


intents = discord.Intents.default()
intents.message_content = True

prefix  = "!"
bot = commands.Bot(command_prefix=prefix , intents=intents)

@bot.event
async def on_ready():
    print(f"Logged into : {bot.user}")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            print(filename)
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())
