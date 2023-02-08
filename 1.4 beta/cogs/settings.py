import disnake
import sqlite3
from disnake.ext import commands
from disnake.enums import ButtonStyle
from disnake import TextInputStyle
from sqlite3 import Error
from embeds import *

create_table = """
CREATE TABLE IF NOT EXISTS settings (
	is_log INTEGER,
	guild_id INTEGER,
	channel_id INTEGER
);
"""

def create_connection(path):
	connection = None
	try:														# Подключиться к базе даннных
		connection = sqlite3.connect(path)
		print("Connection to SQLite DB successful")
	except Error as e:
		print(f"The error '{e}' occurred")

	return connection

def execute_query(query):
	try:
		cursor.execute(query)									# Выполнить действие с таблицой
		connection.commit()
		print("Query executed successfully")
	except Error as e:
		print(f"The error '{e}' occurred")

def write(query):
	try:
		cursor.execute(query)									# Записать данные в таблицу
		connection.commit()
		print("Query executed successfully")
	except Error as e:
		print(f"The error '{e}' occurred")

def execute_read_query(query):
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		return result
	except Error as e:
		print(f"The error '{e}' occurred")

global connection
global cursor

connection = create_connection('settings.db')
cursor = connection.cursor()
execute_query(create_table)

class settings(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
			
	@commands.slash_command()																# Slash command
	async def settings(self, inter):
		await inter.response.send_message(embed = settings_embed, view = buttons())

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

	async def callback(self, inter: disnake.ModalInteraction):									# Callback Modal Window
		if inter.text_values['is_log'] == 'Yes' or inter.text_values['is_log'] == 'yes':			# If 'yes'
			if inter.text_values['channel'].isdigit():													# Проверка на числа
				await inter.response.send_message('Yes')
			else:																						# Если буквы
				await inter.response.send_message(embed = failed_settings_embed)							# То отправляет ошибку
		elif inter.text_values['is_log'] == 'No' or inter.text_values['is_log'] == 'no':			# If 'no'
			
			await inter.response.send_message(embed = off_settings_embed)								# Выключаем отправку логов
		else:																						# Если не 'yes' или не 'no'
			await inter.response.send_message(embed = failed_settings_embed)							# Если нет то отправляет ошибку

def setup(bot: commands.Bot):
	bot.add_cog(settings(bot))