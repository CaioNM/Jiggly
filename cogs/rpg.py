import discord
from discord.ext import commands
from discord import app_commands
import random

class cog3(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  #Rodando dados
  @app_commands.command(name="roll", description="Rola qualquer quantidade de qualquer dado que desejar e soma os resultados")
  async def roll(self, interaction: discord.Interaction, quantidade:int, dado:int):
    i=1
    total = []
    while i<=quantidade:
      i+=1
      rolagem = random.randint(1,dado)
      total.append(rolagem)
      soma = sum(total)
    await interaction.response.send_message(f'{quantidade}d{dado} - **{total}**\nTotal: **{soma}**')


async def setup(client:commands.Bot) -> None:
  await client.add_cog(cog3(client))