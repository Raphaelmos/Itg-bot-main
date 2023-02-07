import disnake
from disnake.ext import commands
from embeds import *
from config import *

bot = commands.Bot(
	command_prefix=".",
	intents=disnake.Intents.all(),
#	test_guilds=[1031065284783648768],
	reload = reload
	)
bot.remove_command("help")
bot.load_extensions('cogs')
print("Cogs is loaded...")


@bot.event
async def on_ready():
	await bot.change_presence(status=disnake.Status.online, activity=disnake.Game("коги!"))
	print("Бот готов!")


@bot.slash_command(description="Перезагрузить коги")
async def reload(inter, extension):
	if inter.author.id == dev_id:
		bot.reload_extension(f"cogs.{extension}")
		print(f"Cog '{extension}' was reloaded")
		await inter.send(f"Ког **{extension}** перезагружен.", ephemeral=True)
	else:
		await inter.send("Вы не имеете право использовать данную команду", ephemeral=True)

@bot.slash_command(description="Выгрузить коги")
async def unload(inter, extension):
	if inter.author.id == dev_id:
		bot.unload_extension(f"cogs.{extension}")
		print(f"Cog '{extension}' was unloaded")
		await inter.send(f"Ког **{extension}** выгружен.", ephemeral=True)
	else:
		await inter.send("Вы не имеете право использовать данную команду", ephemeral=True)


@bot.slash_command(description="Загрузить коги")
async def load(inter, extension):
	if inter.author.id == dev_id:
		bot.load_extension(f"cogs.{extension}")
		print(f"Cog '{extension}' was loaded")
		await inter.send(f"Ког **{extension}** загружен.", ephemeral=True)
	else:
		await inter.send("Вы не имеете право использовать данную команду", ephemeral=True)

@bot.event
async def on_guild_join(guild):
	print(f'Joined to {guild} server')
	await guild.system_channel.send(embed=join_embed)


bot.run(token)