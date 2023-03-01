import disnake
from disnake.ext import commands
from imageParser import *

parser = YandexImage()

class search(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
			
	@commands.slash_command(description = "Ищи любые картинки.")
	async def search(inter, search: str):
		for item in parser.search(search):
			print(item.preview.url)
			await inter.response.send_message(item.preview.url)
			break
			
			



def setup(bot: commands.Bot):
	bot.add_cog(search(bot))