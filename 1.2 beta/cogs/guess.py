import disnake
from disnake.ext import commands
import random
from embeds import *

class guess(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = 'Угадай число')
	async def guess(self, inter, attempt1: int, attempt2: int, attempt3: int, attempt4: int):
		number = round(random.randint(0, 20))
		if attempt1 == attempt2 == attempt3 == attempt4:
			await inter.response.send_message(embed = failed_guess_embed)
		elif attempt1 == attempt2:
			await inter.response.send_message(embed = failed_guess_embed)
		elif attempt1 == attempt3:
			await inter.response.send_message(embed = failed_guess_embed)
		elif attempt1 == attempt4:
			await inter.responce.send_message(embed = failed_guess_embed)
		elif attempt2 == attempt3:
			await inter.response.send_message(embed = failed_guess_embed)
		elif attempt2 == attempt4:
			await inter.response.send_message(embed = failed_guess_embed)
		elif attempt3 == attempt4:
			await inter.response.send_message(embed = failed_guess_embed)
		elif (attempt1 or attempt2 or attempt3 or attempt4) > 20:
			await inter.response.send_message(embed = failed_guess_embed)
		else:
			if number in [attempt1, attempt2, attempt3, attempt4]:
				emb = win_guess_embed
				emb.description = emb.description.format(number = number)
				await inter.response.send_message(embed = emb)
			else:
				emb = lose_guess_embed
				emb.description = emb.description.format(number = number)
				await inter.response.send_message(embed = lose_guess_embed)



def setup(bot: commands.Bot):
	bot.add_cog(guess(bot))