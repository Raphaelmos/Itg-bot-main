import disnake
import sqlite3
from disnake.ext import commands
from disnake.ui import Button
from disnake import TextInputStyle
from embeds import *

connection = sqlite3.connect('settings.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS settings (
	guild INT,
	channel_ID INT,
	is_alarm BIT,
	is_Anty_spam BIT
	)""")

global is_alarm
global is_Anty_spam
global system_channel
is_alarm = False
is_Anty_spam = False
system_channel = None

def get_channel_id(self, serverID):
	cursor.execute(f"""SELECT * from settings WHERE guild=(?)""", (serverID,))
	table = cursor.fetchall()
	try:
		if table[0][2] == 1:
			return self.bot.get_channel(table[0][1])
		else:
			pass
	except IndexError:
		pass

class Alarm(disnake.ui.Modal):
	def __init__(self):
		super().__init__(
			title="Введите информацию",
			custom_id="Alarm_id",
			timeout=300,
			components=[
				disnake.ui.TextInput(
					label="Вы хотите получать уведомления об участниках?",
					placeholder="Yes or No",
					custom_id="isAlarm",
					style=TextInputStyle.short,
					max_length=3
				),
				disnake.ui.TextInput(
					label="System channel ID",
					placeholder="1234567890",
					custom_id="System Channel",
					style=TextInputStyle.short,
					max_length=50,
					required=False
				)
			],
		)

	async def callback(self, inter):
		system_channel = inter.text_values['System Channel']
		if inter.text_values['isAlarm'] == 'Yes':
			if not inter.text_values['System Channel'].isdigit():
				await inter.response.send_message(embed = failed_settings_embed, ephemeral=True)
			else:
				
				async def isMatch():
					cursor.execute(f"""SELECT * from settings WHERE guild=(?)""", (inter.guild.id,))
					records = cursor.fetchall()
					async def try_rec():
						try:
							return records[0][0]
						except IndexError:
							return False

					if await try_rec() == inter.guild.id:
						return True
					else:
						return False

				if await isMatch():
					is_alarm = True
					cursor.execute(f'''UPDATE settings SET is_alarm=?, channel_ID=? WHERE guild=?;''', (is_alarm, inter.text_values['System Channel'], inter.guild.id))
					connection.commit()
					await inter.response.send_message(embed = changed_settings_embed, ephemeral=True)
				else:
					is_alarm = True
					cursor.execute(f'''INSERT INTO settings VALUES (?, ?, ?, ?)''', (inter.guild.id, inter.text_values['System Channel'], is_alarm, is_Anty_spam)) 
					connection.commit()
					await inter.response.send_message(embed = table_settings_embed, ephemeral=True)
		elif inter.text_values['isAlarm'] == 'No':
			is_alarm = False
			cursor.execute(f'''UPDATE settings SET is_alarm=? WHERE guild=?;''', (is_alarm, inter.guild.id))
			connection.commit()
			await inter.response.send_message(embed = off_settings_embed, ephemeral=True)
		else:
			pass


class Anty_spam(disnake.ui.Modal):
	def __init__(self):
		components = [
		disnake.ui.TextInput(
			label="Anty_spam",
			placeholder="Yes/No",
			custom_id="is_Anty_spam",
			style=TextInputStyle.short,
			max_length=3,
			),
		]
		super().__init__(
			title="Введите информацию",
			custom_id="Anty_spam_id",
			components=components,
			)

	async def callback(self, inter: disnake.ModalInteraction):
		if not inter.text_values['is_Anty_spam'].isdigit():
			if inter.text_values['is_Anty_spam'] == 'Yes':
				
				async def isMatch():
					cursor.execute(f"""SELECT * from settings WHERE guild=(?)""", (inter.guild.id,))
					records = cursor.fetchall()
					async def try_rec():
						try:
							return records[0][0]
						except IndexError:
							return False
					if await try_rec() == inter.guild.id:
						return True
					else:
						return False
				
				if await isMatch():
					is_Anty_spam = True
					cursor.execute(f'''UPDATE settings SET is_Anty_spam=? WHERE guild=?;''', (is_Anty_spam, inter.guild.id))
					connection.commit()
					await inter.response.send_message(embed = changed_settings_embed, ephemeral=True)

				else:
					is_Anty_spam = True
					cursor.execute(f'''INSERT INTO settings VALUES (?, ?, ? , ?)''', (inter.guild.id, system_channel, is_alarm, is_Anty_spam)) 
					connection.commit()
					await inter.response.send_message(embed = table_settings_embed, ephemeral=True)

			elif inter.text_values['is_Anty_spam'] == 'No':
				is_Anty_spam = False
				cursor.execute(f'''UPDATE settings SET is_Anty_spam=? WHERE guild=?;''', (is_Anty_spam, inter.guild.id))
				connection.commit()
				await inter.response.send_message(embed = off_settings_embed, ephemeral=True)
		else:
			await inter.response.send_message(embed = failed_settings_embed, ephemeral = True)

class Settings(disnake.ui.View):
	def __init__(self):
		super().__init__()

	@disnake.ui.button(label="Оповещения", style=disnake.ButtonStyle.green, emoji="☎️")
	async def Alarm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
		await inter.response.send_modal(modal=Alarm())

	@disnake.ui.button(label="Антиспам", style=disnake.ButtonStyle.green, emoji="📬")
	async def Anty_spam(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
		await inter.response.send_modal(modal=Anty_spam())

class settings(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
	
	@commands.slash_command(description = "Настройки бота", default_member_permissions=disnake.Permissions(administrator=True))
	async def settings(self, inter):
		await inter.response.send_message(embed = settings_embed, view=Settings(), ephemeral=True)
			
	@commands.Cog.listener()
	async def on_member_join(self, member):
		try:
			server = member.guild.id
			channel = get_channel_id(self, server)
			emb = member_join_settings_embed
			emb.description = emb.description.format(member = member.mention)
			await channel.send(embed = emb)
		except AttributeError:
			pass

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		try:
			server = member.guild.id
			channel = get_channel_id(self, server)
			emb = member_remove_settings_embed
			emb.description = emb.description.format(member = member.mention, joined_at = member.joined_at)
			emb.description = str(emb.description)[:-21]
			await channel.send(embed = emb)
		except AttributeError:
			pass

	@commands.Cog.listener()
	async def on_message(self, message):
		global tek_msg
		tek_msg = None
		cursor.execute(f"""SELECT * from settings WHERE guild=(?)""", (message.guild.id,))
		table = cursor.fetchall()
		try:
			if table[0][3] == 1:
				print(tek_msg)
				if tek_msg == message.content:
					print("1")
					tek_msg = message.content
				else:
					print("0")
					tek_msg = message.content
			else:
				pass
		except IndexError:
			pass


def setup(bot: commands.Bot):
	bot.add_cog(settings(bot))