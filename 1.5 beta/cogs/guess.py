import disnake
from disnake.ext import commands
import random
from embeds import *

class guess(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(name='guess_the_number', description='Угадай число')
	async def guess(inter: disnake.AppCmdInter, attempt1: int, attempt2: int, attempt3: int, attempt4: int):
		attemps = {attempt1, attempt2, attempt3, attempt4}
		numbers = [attempt1, attempt2, attempt3, attempt4]
		for i in numbers:
			if i < 21:
				is_number = True
			else:
				is_number = False
				break

		if is_number:
			if len(attemps) < 4:
				await inter.response.send_message(embed=failed_guess_embed)
			else:
				number = random.randint(0, 20)
				if len([i for i in attemps if i == number]) > 0:
					emb = win_guess_embed
					emb.description = emb.description.format(number = number)
					await inter.response.send_message(embed=win_guess_embed)
				else:
					emb = lose_guess_embed
					emb.description = emb.description.format(number = number)
					await inter.response.send_message(embed=lose_guess_embed)
		else:
			await inter.response.send_message(embed=failed_guess_embed)



def setup(bot: commands.Bot):
	bot.add_cog(guess(bot))