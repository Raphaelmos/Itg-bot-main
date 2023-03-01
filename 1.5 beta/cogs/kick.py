import disnake
from disnake.ext import commands
from embeds import *

class kick(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = "Кикнуть пользователя", default_member_permissions=disnake.Permissions(kick_members=True))
	async def kick(self, inter, member: disnake.Member, *, reason = None):
		try:
			await member.kick(reason = reason)
			emb = kick_embed
			emb.description = emb.description.format(member = member.mention, reason = reason)
			await inter.response.send_message(embed = emb)
		except disnake.errors.Forbidden:
			await inter.response.send_message(embed = missing_permissions_embed)


def setup(bot: commands.Bot):
	bot.add_cog(kick(bot))