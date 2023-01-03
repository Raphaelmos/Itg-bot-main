import disnake
from disnake.ext import commands
from embeds import *

def secure_eval(action):
	is_true = 0
	allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']
	for i in range(len(action)):
		if action[i] in allowed:
			is_true=1
		else:
			is_true=0
			break

	if is_true:
		return eval(action)
	else:
		return "Я не могу выполнить данную команду"

allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']

'''def secure_eval(action):
    if not any([letter for letter in action if letter in allowed]):
        return eval(action)
    return "Я не могу выполнить данную команду"'''

class calc(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		
	@commands.slash_command(description = "Вычислить что-либо")
	async def calc(self, inter, to_do: str):
		await inter.response.send_message(secure_eval(to_do))

def setup(bot: commands.Bot):
	bot.add_cog(calc(bot))