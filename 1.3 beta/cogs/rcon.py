import disnake
import asyncio
from disnake.ext import commands
from aiomcrcon import Client
from config import ip, port, password

class rcon(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command(description = "Add member", default_member_permissions=disnake.Permissions(administrator=True))
    async def whitelist_add(self, inter, member: disnake.Member):
        if inter.guild.id == 978144424540389386:
            command = f'easywl add  {member.name}'
            client = Client(ip, port, password)
            await client.connect()
            responses = await client.send_cmd(command)
            print(responses)
            await client.close()
            await inter.response.send_message("Участник успешно добавлен.", ephemeral=True)
        else:
            await inter.response.send_message("Эта команда не преднозначена для данного сервера. Попросите вледельца бота подключить вас.")

    @commands.slash_command(description = "Remove member", default_member_permissions=disnake.Permissions(administrator=True))
    async def whitelist_remove(self, inter, member: disnake.Member):
        if inter.guild.id == 978144424540389386:
            command = f'easywl remove  {member.name}'
            client = Client(ip, port, password)
            await client.connect()
            responses = await client.send_cmd(command)
            print(responses)
            await client.close()
            await inter.response.send_message("Участник успешно удален.", ephemeral=True)
        else:
            await inter.response.send_message("Эта команда не преднозначена для данного сервера. Попросите вледельца бота подключить вас.")

    @commands.slash_command(description = "Rcon", default_member_permissions=disnake.Permissions(administrator=True))
    async def rcon_exec(self, inter, to_do):
        if inter.guild.id == 978144424540389386:
            command = f'{to_do}'
            client = Client(ip, port, password)
            await client.connect()
            responses = await client.send_cmd(command)
            await client.close()
            await inter.response.send_message(f"Команда выполнена. {responses}", ephemeral=True)
        else:
            await inter.response.send_message("Эта команда не преднозначена для данного сервера. Попросите вледельца бота подключить вас.")


def setup(bot: commands.Bot):
    bot.add_cog(rcon(bot))