import disnake
import openai
from disnake.ext import commands
from config import api_key, model_engine

openai.api_key = api_key
model_engine = model_engine

class gpt(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.slash_command()
    async def chat_gpt(self, inter, task: str):
        await inter.response.send_message(f'Вопрос: {task}')
        message = await inter.channel.send('ChatGPT думает...')
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=task,
            max_tokens=4097-len(task),
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        await message.edit(completion.choices[0].text)


def setup(bot: commands.Bot):
    bot.add_cog(gpt(bot))