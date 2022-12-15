import os
import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import platform

class Client(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix=commands.when_mentioned_or('>'), intents = discord.Intents(members = True, presences = True).all())

    self.cogslist = ["cogs.aleatorios", "cogs.rpg", "cogs.estruturais"]
  async def setup_hook(self):
    for ext in self.cogslist:
      await self.load_extension(ext)

  async def on_ready(self):
    prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S GMT", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print("\n" + prfx + " Loggado como: " + Fore.YELLOW + self.user.name)
    print(prfx + " ID: " + Fore.YELLOW + str(self.user.id))
    print(prfx + " Versão do Discord: " + Fore.YELLOW + discord.__version__)
    print(prfx + " Versão do Python: " + Fore.YELLOW + str(platform.python_version()))
    print("\n  ✨ Jiggly use Lullaby ✨\n")
    synced = await self.tree.sync()
    print(prfx + " Slash Commands sincronizados! " + Fore.YELLOW + str(len(synced)) + " Comandos")  

client = Client()
client.run(os.getenv("TOKEN"))