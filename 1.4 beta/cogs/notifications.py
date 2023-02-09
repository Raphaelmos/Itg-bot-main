import disnake
import sqlite3
from disnake.ext import commands
from sqlite3 import Error
from embeds import *

global connection
global cursor

connection = sqlite3.connect('settings.db')
cursor = connection.cursor()

class notifications(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_member_join(self, member):
        cursor.execute(f"""SELECT is_log, channel_id from settings WHERE guild_id = {member.guild.id}""")
        result = cursor.fetchall()
        try:
            if result[0][0] == 1:
                channel_id = result[0][1]
                channel = self.bot.get_channel(channel_id)
                emb = member_join_settings_embed
                emb.description = emb.description.format(member = member.mention)
                await member.guild.system_channel.send(embed = emb)
            else:
                pass
        except AttributeError:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        cursor.execute(f"""SELECT is_log, channel_id from settings WHERE guild_id = {member.guild.id}""")
        result = cursor.fetchall()
        try:
            if result[0][0] == 1:
                channel_id = result[0][1]
                channel = self.bot.get_channel(channel_id)
                emb = member_remove_settings_embed
                emb.description = emb.description.format(member = member.mention, joined_at = str(member.joined_at)[0:11])
                await member.guild.system_channel.send(embed = emb)
            else:
                pass
        except AttributeError:
            pass

def setup(bot: commands.Bot):
    bot.add_cog(notifications(bot))