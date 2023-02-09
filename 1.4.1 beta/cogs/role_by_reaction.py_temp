import disnake
from disnake.ext import commands
from embeds import *


class role_by_reaction(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = " Выдать роль за нажатие н реакцию.", default_member_permissions=disnake.Permissions(administrator=True))
	async def role_by_reaction(self, interaction, message: str, reaction: str, role: disnake.Role):
		global emoji
		global name_role
		global user
		emoji = reaction
		name_role = role
		user = interaction.author

		try:
			msg = await interaction.channel.send(message)
			await msg.add_reaction(reaction)
			await interaction.response.send_message('Роль за реакцию успешно добавленно.', ephemeral=True)
		except disnake.errors.HTTPException:
			await interaction.channel.purge(limit = 1)
			await interaction.response.send_message('Я не знаю такого смайлика. Попробуйте еще раз.', ephemeral=True)

	@commands.Cog.listener()
	async def on_reaction_add(self,  reaction, user):
		try:
			if not reaction == emoji: # reaction != emoji
				if str(user) == 'ITG-bot BETA#1790':
					pass
				else:
					await user.add_roles(name_role)
					await user.send(f"Роль **<{name_role}>** была взята.")
			else:
				pass

		except disnake.errors.Forbidden:
			await user.send(embed = missing_permissions_embed)
		
	@commands.Cog.listener()
	async def on_reaction_remove(reaction, user):
		print("Reaction remove")
		try:
			if not reaction == emoji: # reaction != emoji
				if str(user) == 'ITG-bot BETA#1790':
					pass
				else:
					await user.remove_role(name_role, atomic=True)
					await user.send(f"Роль **<{name_role}>** была снята.")
			else:
				pass

		except disnake.errors.Forbidden:
			await user.send(embed = missing_permissions_embed)
			



def setup(bot: commands.Bot):
	bot.add_cog(role_by_reaction(bot))