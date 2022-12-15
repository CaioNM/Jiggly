import discord
from discord.ext import commands
from discord import app_commands


class cog1(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client


  #Comando de teste
  @app_commands.command(name="ping", description="Mostra o tempo de resposta")
  async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message(content=f'Pong!  🏓\nPing de {round(self.client.latency * 1000)}ms!')

  #Desligando o bot por comando
  @app_commands.command(name="mimir", description="Desliga o bot")
  async def mimir(self, interaction: discord.Interaction):
    await interaction.response.send_message(content="Mimindo......")
    await self.client.close()


async def setup(client:commands.Bot) -> None:
  await client.add_cog(cog1(client))