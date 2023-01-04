import disnake
from disnake.ext import commands
from embeds import *

class send_private(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
            
  @commands.slash_command()
  async def send_private(self, inter):
    await inter.author.send("Hello from ITG bot!")
    await inter.response.send_message("Посмотри ЛС!")
        



def setup(bot: commands.Bot):
  bot.add_cog(send_private(bot))