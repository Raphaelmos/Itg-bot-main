import disnake
import sqlite3
from disnake.ext import commands
from sqlite3 import Error
from embeds import *

global connection
global cursor

connection = sqlite3.connect('role_by_reaction.db')
print("Connection to SQLite DB role_by_reaction successful")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS role_by_reaction (mmessage_id INTEGER, role_id INTEGER, emoji TEXT);""")
connection.commit()

class role_by_reaction(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						

	@commands.slash_command()
	async def role_by_reaction(self, inter, text: str, role: disnake.Role, emoji: str):
		try:
			emb = r_b_r_embed
			emb.description = emb.description.format(message = text)
			message = await inter.channel.send(embed = emb)
			await message.add_reaction(emoji)
			cursor.execute(f"""INSERT INTO role_by_reaction (mmessage_id, role_id, emoji) VALUES ({message.id}, {role.id}, '{emoji}');""")
			connection.commit()
			await inter.response.send_message("Успешно", ephemeral = True)
		except disnake.errors.HTTPException:
			await inter.channel.purge(limit = 1)
			await inter.response.send_message("Я не знаю такого эмодзи", ephemeral = True)
		except Error as e:
			print(f'{e}')
			await inter.channel.purge(limit = 1)
			await inter.response.send_message("Произошла ошибка записи.", ephemeral = True)



def setup(bot: commands.Bot):
	bot.add_cog(role_by_reaction(bot))