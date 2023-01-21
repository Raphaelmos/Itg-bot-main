import disnake
import sqlite3
from disnake.ext import commands
from disnake.enums import ButtonStyle
from disnake import TextInputStyle
from sqlite3 import Error
from embeds import *

try:
    connection = sqlite3.connect('settings.db')
    print("Connection to SQLite DB successful")

    cursor = connection.cursor()

    create_table = """
    CREATE TABLE IF NOT EXISTS users (
        is_alarm INT
    );
    """

    cursor.execute(create_table)
    connection.commit()
    print("Query executed successfully")

except Error as e:
    print(f"The error '{e}' occurred")

class settings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.slash_command()
    async def settings(self, inter):
        await inter.response.send_message(embed = settings_embed, view = buttons())

class buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(label="Логи", style=ButtonStyle.red, emoji='🔔')
    async def first_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.send_modal(MyModal())

class MyModal(disnake.ui.Modal):
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
        await inter.response.send_message("Таблица успешно записана.")

def setup(bot: commands.Bot):
    bot.add_cog(settings(bot))