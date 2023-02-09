import disnake
import sqlite3
from disnake.ext import commands
from disnake.enums import ButtonStyle
from disnake import TextInputStyle
from sqlite3 import Error
from embeds import *

global connection
global cursor

connection = sqlite3.connect('settings.db')
print("Connection to SQLite DB successful")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS settings (is_log INTEGER, guild_id INTEGER, channel_id INTEGER);""")
connection.commit()

class settings(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
			
	@commands.slash_command(description="Настройки бота", default_member_permissions=disnake.Permissions(administrator=True))																# Slash command
	async def settings(self, inter):
		await inter.response.send_message(embed = settings_embed, view = buttons(), ephemeral=True)

class buttons(disnake.ui.View):																# Buttons
	def __init__(self):
		super().__init__(timeout=None)
	
	@disnake.ui.button(label="Логи", style=ButtonStyle.red, emoji='🔔')
	async def first_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
		await inter.response.send_modal(MyModal())

class MyModal(disnake.ui.Modal):															# Modal Window
	def __init__(self):
		components = [
			disnake.ui.TextInput(
				label="Вы хотите получать оповещения?",
				placeholder="Yes/No",
				custom_id="is_log",
				style=TextInputStyle.short, 
				max_length=3,
			),
			disnake.ui.TextInput(
				label="Id канала для отправки логов",
				placeholder="1234567890",
				custom_id="channel",
				style=TextInputStyle.short,
			),
		]
		super().__init__(
			title="Логи",
			custom_id="logs",
			components=components,
		)

	async def callback(self, inter: disnake.ModalInteraction):
		try:
			if inter.text_values['is_log'] == 'Yes' or inter.text_values['is_log'] == 'yes':
				if inter.text_values['channel'].isdigit():
					cursor.execute(f"""SELECT * from settings WHERE guild_id = {inter.guild.id}""")
					result = cursor.fetchall()
					if len(result) == 0:
						cursor.execute(f"""INSERT INTO settings (is_log, guild_id, channel_id) VALUES (1, {inter.guild.id}, {inter.text_values['channel']});""")
						connection.commit()
						await inter.response.send_message(embed = table_settings_embed, ephemeral=True)
					elif len(result) > 0:
						cursor.execute(f"""UPDATE settings SET is_log = 1, channel_id = {inter.text_values['channel']} WHERE guild_id = {inter.guild.id}""")
						connection.commit()
						await inter.response.send_message(embed = changed_settings_embed, ephemeral=True)
				else:
					await inter.response.send_message(embed = failed_settings_embed, ephemeral=True)
			elif inter.text_values['is_log'] == 'No' or inter.text_values['is_log'] == 'no':
				cursor.execute(f"""SELECT * from settings WHERE guild_id = {inter.guild.id}""")
				result = cursor.fetchall()
				if len(result) == 0:
					cursor.execute(f"""INSERT INTO settings (is_log, guild_id, channel_id) VALUES (0, {inter.guild.id}, 00000);""")
					connection.commit()
				elif len(result) > 0:
					cursor.execute(f"""UPDATE settings SET is_log = 0 WHERE guild_id = {inter.guild.id}""")
					connection.commit()
				await inter.response.send_message(embed = off_settings_embed, ephemeral=True)
			else:
				await inter.response.send_message(embed = failed_settings_embed, ephemeral=True)
		except Error as e:
			print(f"The error '{e}' occurred")

def setup(bot: commands.Bot):
	bot.add_cog(settings(bot))