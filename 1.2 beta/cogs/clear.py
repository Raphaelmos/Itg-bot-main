import disnake
from disnake.ext import commands
from embeds import *

class clear(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = "Очистить чат", default_member_permissions=disnake.Permissions(manage_messages=True))
	async def clear(self, inter, amount: int):
		if amount > 100:
			emb = failed_clear_embed
			await inter.response.send_message(embed = emb)
		else:
			try:
				await inter.channel.purge(limit = amount)
				emb = clear_embed
				emb.description = emb.description.format(amount = amount)
				await inter.response.send_message(embed = emb)
			except disnake.errors.Forbidden:
				await inter.response.send_message(embed = missing_permissions_embed)
			
def setup(bot: commands.Bot):
	bot.add_cog(clear(bot))