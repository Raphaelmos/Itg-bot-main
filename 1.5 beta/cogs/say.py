import disnake
from disnake.ext import commands
from embeds import *

class say(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = "Сказать через бота")
	async def say(self, inter, text: str):
		#emoji = str(self.bot.get_emoji(1034205872982859797))
		emb = say_embed
		emb.description = emb.description.format(text = text)
		await inter.response.send_message(embed = emb)



def setup(bot: commands.Bot):
	bot.add_cog(say(bot))