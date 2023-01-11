import disnake
from disnake.ext import commands

class nsfw(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.slash_command()
    async def nsfw(inter):
        await inter.response.send_message(file=disnake.File('logo.png'))



def setup(bot: commands.Bot):
    bot.add_cog(nsfw(bot))