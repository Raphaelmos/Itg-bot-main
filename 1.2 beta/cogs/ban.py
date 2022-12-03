import disnake
from disnake.ext import commands
from embeds import *


class ban(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.slash_command(description="Забанить пользователя", default_member_permissions=disnake.Permissions(ban_members=True))
	async def ban(self, inter, member: disnake.Member, *, reason: str):
		try:
			await member.ban(reason=reason)
			emb = ban_embed
			emb.description = emb.description.format(member=member, reason=reason)
			await inter.response.send_message(embed=emb)
		except disnake.errors.Forbidden:
			await inter.response.send_message(embed=missing_permissions_embed)


def setup(bot: commands.Bot):
	bot.add_cog(ban(bot))
