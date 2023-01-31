import disnake
from disnake.ext import commands
from memory_profiler import memory_usage
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


class info(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = "Информация о боте",)
	async def info(self, inter):
		ping = f"**{round(self.bot.latency * 1000)}мс**"
		RAM = f"**{round(memory_usage()[0])} мб**"
		date = "**24.09.2022**"
		dev = "**IvanTopGaming#2635**"
		version = "**1.4 beta**"

		emb = info_embed
		emb.description = emb.description.format(ping = ping, RAM = RAM, date = date, dev = dev, version = version)
		await inter.response.send_message(embed = emb, view = ButtonAccept())



def setup(bot: commands.Bot):
	bot.add_cog(info(bot))