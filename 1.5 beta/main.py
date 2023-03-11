import disnake
import asyncio
from disnake.ext import commands
from embeds import *
from config import *

bot = commands.Bot(
	command_prefix=".",
	intents=disnake.Intents.all(),
#	test_guilds=[1031065284783648768],
	reload = reload,
	sync_commands_debug = True
	)
bot.remove_command("help")
bot.load_extensions('cogs')
print("Cogs is loaded...")


@bot.event
async def on_ready():
	print(f'Logged on as {bot.user}!')
	print("Бот готов!")
	await bot.change_presence(status=disnake.Status.online, activity=disnake.Game("коги!"))

@bot.event
async def on_guild_join(guild):
	print(f'Joined to {guild} server')
	await guild.system_channel.send(embed=join_embed)


bot.run(token)