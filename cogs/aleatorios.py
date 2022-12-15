import discord
from discord.ext import commands
from discord import app_commands
import datetime

class cog2(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  #User Info command
  @app_commands.command(name="userinfo", description="Manda informações do usuário desejado")
  async def userinfo(self, interaction: discord.Interaction, member:discord.Member=None):
    if member == None:
      member = interaction.user
    roles = [roles for roles in member.roles]
    embed = discord.Embed(title="Informações do Usuário", description=f"Aqui estão as informações do(a) {member.mention}", color = discord.Color.from_rgb(168, 62, 207), timestamp = datetime.datetime.utcnow())
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="Nome:", value = f'{member.name}#{member.discriminator}')
    embed.add_field(name="Apelido:", value = member.display_name)
    embed.add_field(name='ID:', value = member.id)
    embed.add_field(name='Status:', value = member.status)
    embed.add_field(name="Criado em:", value=member.created_at.strftime("%a, %d/%m/%Y, %I:%M %p"))
    embed.add_field(name="No server desde:", value=member.joined_at.strftime("%a, %d/%m/%Y, %I:%M %p"))
    embed.add_field(name=f"Cargos ({len(roles)-1}):", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Maior Cargo:", value=member.top_role.mention)
    if member.bot == True:
      teste = "Sim 🤖"
    else:
      teste = "Não!"
    embed.add_field(name="Bot?", value=teste)
    await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(client:commands.Bot) -> None:
  await client.add_cog(cog2(client))