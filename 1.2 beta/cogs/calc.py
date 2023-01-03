import disnake
from disnake.ext import commands
import decimal
import re
from decimal import *
from embeds import *

def getNumbers(to_do):
	final = re.findall(r'[0-9]+', to_do)
	do = re.search(r"\W", to_do)
	result = eval(f'Decimal(final[0]) {do[0]} Decimal(final[1])')
	return result

class calc(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		
	@commands.slash_command(description = "Вычислить что-либо")
	async def calc(self, inter, to_do: str):
		allowed = ["+", "-", "*", "/", " ", "**", ".", "(", ")"]
		def check(text: str):
			if len([b for b in text if b.isdigit() or b in allowed]) == len(text):
				final = re.findall(r'[0-9]+', to_do)
				if len(final) == 2:
					return True
				else:
					return False
			else:
				return False
		
		if check(to_do):
			calc_embed = disnake.Embed(
				title="Calc",
				description=f"Итак: \n``{to_do}`` будет: \n\n**``{getNumbers(to_do)}``**",
				colour=0xF0C43F,
				)
			await inter.response.send_message(embed = calc_embed)
		else:
			emb = failed_calc_embed
			await inter.response.send_message(embed = failed_calc_embed)

def setup(bot: commands.Bot):
	bot.add_cog(calc(bot))