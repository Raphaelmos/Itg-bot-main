import disnake
from disnake.ext import commands
from embeds import *


class Dropdown(disnake.ui.StringSelect):
	def __init__(self):
		options = []
		for i in users:
			options.append(disnake.SelectOption(label=f'{i}', description="Разбанить пользователя", emoji="🔓"))

		super().__init__(
			placeholder="Выберите участника.",
			max_values=1,
			options=options,
		)

	async def callback(self, inter: disnake.MessageInteraction):
		await inter.guild.unban(id)
		emb = unban_embed
		emb.description = emb.description.format(member = self.values[0])
		await inter.response.send_message(embed = emb)


class DropdownView(disnake.ui.View):
	def __init__(self):
		super().__init__()
		self.add_item(Dropdown())



class unban(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = "Разбанить пользователя", default_member_permissions=disnake.Permissions(ban_members=True))
	async def unban(self, inter):
		try:
			ban_list = await inter.guild.bans(limit=25).flatten()
			if not len(ban_list) == 0:
				global users
				users = []
				for i in range(0, len(ban_list)):
					user = ban_list[i][1].name
					id = await self.bot.fetch_user(ban_list[i][1].id)
					users.append(user)

				await inter.response.send_message(embed = msg_unban_embed, view=DropdownView(), ephemeral=True)
			else:
				await inter.response.send_message(embed = failed_unban_embed, ephemeral=True)
		except disnake.errors.Forbidden:
			await inter.response.send_message(embed = missing_permissions_embed, ephemeral=True)


def setup(bot: commands.Bot):
	bot.add_cog(unban(bot))