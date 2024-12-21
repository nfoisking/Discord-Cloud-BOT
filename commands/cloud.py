import discord
from discord import app_commands
from discord.ext import commands
import requests

class CloudCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="cloud", description="nigger")
    @app_commands.describe(input_value="Puxar algo")
    async def cloud(self, interaction: discord.Interaction, input_value: str):
        await interaction.response.defer(ephemeral=True)
        try:
            data = {
                "token": "your key",
                "request": input_value,
                "limit": 10000,
                "lang": "en"
            }
            url = 'https://leakosintapi.com/'

            response = requests.post(url, json=data)
            response_data = response.json()

            file_path = "cloud.txt"
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(str(response_data))

            with open(file_path, "rb") as file:
                await interaction.followup.send(
                    file=discord.File(file, filename="cloud.txt"),
                    ephemeral=True
                )
        except Exception as e:
            await interaction.followup.send(
                content=f"{str(e)}",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(CloudCommand(bot))