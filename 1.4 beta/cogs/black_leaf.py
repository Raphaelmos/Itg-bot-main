import disnake
from disnake.ext import commands
from embeds import *
from config import *

black_guilds=black_guilds

class black_leaf(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		for guild in self.bot.guilds:
			for i in range(0, len(black_guilds)):
				if guild.owner.id == black_guilds[i] or guild.id == black_guilds[i]:
					emb = black_leaf_embed
					await guild.system_channel.send(embed = black_leaf_embed)
					await guild.leave()



def setup(bot: commands.Bot):
		bot.add_cog(black_leaf(bot))