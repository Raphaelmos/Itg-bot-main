import disnake
from disnake.ext import commands
from embeds import *

class mute(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = "Замьютить пользователя", default_member_permissions=disnake.Permissions(mute_members=True))
	async def mute(self, inter, member: disnake.Member, time: int, reason: str):
		try:
			await member.timeout(duration = time*60, reason = reason)
			emb = mute_embed
			emb.description = emb.description.format(member = member.mention, time = time, reason = reason)
			await inter.response.send_message(embed = emb)
		except disnake.errors.Forbidden:
			await inter.response.send_message(embed = missing_permissions_embed)


def setup(bot: commands.Bot):
	bot.add_cog(mute(bot))