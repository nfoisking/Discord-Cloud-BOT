import discord
from discord.ext import commands
import json
import os
from colorama import init, Fore

with open('config.json') as f:
    config = json.load(f)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all(), application_id="1315801758567764090")

    async def setup_hook(self):
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                await self.load_extension(f'commands.{filename[:-3]}')

        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    os.system("cls")
    print(f"{bot.user.name}")
    await bot.change_presence(activity=discord.Game(name="Lost Searcher | v1.0"))

bot.run(config['token'])