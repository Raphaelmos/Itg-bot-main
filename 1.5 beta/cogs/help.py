import disnake
from disnake.ext import commands
from disnake.ui import Button
from embeds import *

class ButtonAccept(disnake.ui.View):
	def __init__(self):
		super().__init__()

	@disnake.ui.button(label="Сервер", style=disnake.ButtonStyle.url, emoji="🛰️", url = "https://discord.gg/6WSkDfhUWC")
	async def button(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
		pass
		
	@disnake.ui.button(label="GitHub", style=disnake.ButtonStyle.url, emoji="💾", url = "https://github.com/IvanTopGaming/Itg-bot-main")
	async def button2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
		pass

class help(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.slash_command(description="Помощь по командам", )
	async def help(self, inter):
		await inter.response.send_message(embed = help_embed, view = ButtonAccept())


def setup(bot: commands.Bot):
	bot.add_cog(help(bot))