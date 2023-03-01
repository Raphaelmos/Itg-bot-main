import disnake
import openai
from disnake.ext import commands

openai.api_key = "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"
model_engine = "text-davinci-003"

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
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        await message.edit(completion.choices[0].text)


def setup(bot: commands.Bot):
    bot.add_cog(gpt(bot))