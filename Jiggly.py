import os
import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import datetime
import platform
import random

client = commands.Bot(command_prefix = ">", intents=discord.Intents.all())

@client.event
async def on_ready():
  prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S GMT", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
  print(prfx + " Loggado como: " + Fore.YELLOW + client.user.name)
  print(prfx + " ID: " + Fore.YELLOW + str(client.user.id))
  print(prfx + " Versão do Discord: " + Fore.YELLOW + discord.__version__)
  print(prfx + " Versão do Python: " + Fore.YELLOW + str(platform.python_version()))
  print("\n  ✨ Jiggly use Lullaby ✨\n")
  synced = await client.tree.sync()
  print(prfx + " Slash Commands sincronizados! " + Fore.YELLOW + str(len(synced)) + " Comandos")

#Comando de teste
@client.tree.command(name="ping", description="Mostra o tempo de resposta")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(content=f'Pong!  🏓\nPing de {round(client.latency * 1000)}ms!')

#Desligando o bot por comando
@client.tree.command(name="mimir", description="Desliga o bot")
async def mimir(interaction: discord.Interaction):
  await interaction.response.send_message(content="Mimindo......")
  await client.close()

#User Info command
@client.tree.command(name="userinfo", description="Manda informações do usuário desejado")
async def userinfo(interaction: discord.Interaction, member:discord.Member=None):
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

#Rodando dados
@client.tree.command(name="roll", description="Rola qualquer quantidade de qualquer dado que desejar e soma os resultados")
async def roll(interaction: discord.Interaction, quantidade:int, dado:int):
    i=1
    total = []
    while i<=quantidade:
      i+=1
      rolagem = random.randint(1,dado)
      total.append(rolagem)
      soma = sum(total)
    await interaction.response.send_message(f'{quantidade}d{dado} - **{total}**\nTotal: **{soma}**')

client.run(os.getenv("TOKEN"))