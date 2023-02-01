import disnake
from disnake.ext import commands
from disnake.utils import get
from embeds import *

class rules(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
						
	@commands.slash_command(description = "Сказать через бота")
	async def rules(self, inter):
		emb = disnake.Embed(
			title = "Правила",
			description = """**ГЛАВА 1 — ОСНОВНЫЕ ПОЛОЖЕНИЯ**

• 1.1 — Данные правила действуют только на сервере Vanilka/az, за исключением пункта 2.3.1.
• 1.2 — Правила могут изменяться, не упоминая пользователей сервера.
• 1.3 — Администрация вправе выдавать наказания вне рамок данных правил, но по адекватной причине.
• 1.4 — Администрация может добавить вас в Чёрный Список сервера на своё усмотрение.
• 1.5 — На некоторых каналах установлены свои правила, такие как оффтоп.
• 1.6 — Запрещена передача аккаунта третьим лицам.
• 1.7 — Запрещено обходить наказание левым аккаунтом или использовать твинк в злостных целях.

**ГЛАВА 2 — ОСНОВНЫЕ ПРАВИЛА СЕРВЕРА**

• 2.1 — Любые оскорбления и угрозы в сторону пользователя или его родственников запрещены.
(Исключение: Дружеские оскорбления, которые не несут цели унизить человека.)
• 2.2 — Запрещено аморальное и неадекватное поведение.
• 2.3 — Запрещена любая реклама сторонних проектов, а также распространение IP и ссылки серверов, каналов, не связанных с этим сервером. Также запрещена любая коммерческая деятельность за реальные деньги.
• 2.3.1 — Запрещён фишинг, вредоносные ссылки и любого вида мошенничество.
• 2.3.2 — Любая скрытая реклама запрещена и её намёки.
• 2.4 — Запрещено провоцировать пользователя любыми методами на конфликт.
• 2.4.1 — Запрещен троллинг участников чата (наказание выдается только по жалобе).
• 2.5 — Запрещена дезинформация пользователей сервера.
• 2.6 — Запрещено распространять личную информацию участника сервера.
• 2.7 — Запрещено спойлерить события в фильмах, играх и т.д.
• 2.8 — Запрещены разговоры на тему: расизм, разжигание религиозной розни, фашизм, терроризм, наркотические вещества, политика, суицид.
• 2.9 — Запрещено оскорбление сервера.
• 2.10 — Запрещено попрошайничество реальных денег, ролей, пиара, размута.
• 2.11 — Запрещен призыв на нарушение правил.

**ГЛАВА 3 — ПРАВИЛА ТЕКСТОВЫХ КАНАЛОВ**

• 3.1 — Запрещён флуд (в том числе флуд символами), флейм, чрезмерное повторение сообщений других пользователей, а также запрещено отправлять сообщения, засоряющие чат.
• 3.1.1 — Запрещена намеренная организация флуда.
• 3.1.2 — Запрещен мульти-постинг.
• 3.2 — Запрещено отправлять раздражительные (с громким звуком или мелькают) и оскорбительные эмодзи, фото, GIF, видео.
• 3.3 — Запрещено присылать жестокий, кровопролитый, порнографический контент.
• 3.4 — Запрещены любые сообщения, стимулирующие остановку чата.
• 3.5 — Запрещено Ставить на паузу/Скипать/Включать музыку без согласия остальных слушателей.
• 3.6 — Запрещено намеренно разговаривать на иностранных языках.
• 3.7 — Запрещён пинг роли без уважительной причины, чрезмерный пинг пользователя.
• 3.7.1 — Запрещено вызывать админа без причины.
• 3.8 — Запрещено злоупотреблять капсом.

**ГЛАВА 4 — ПРАВИЛА ГОЛОСОВЫХ КАНАЛОВ**

• 4.1 — Запрещено злоупотреблять матом, использовать мат в оскорбительных целях.
• 4.2 — Запрещены громкие/резкие/раздражительные звуки.
• 4.3 — Запрещены постоянные переходы из одного канала в другой.
• 4.4 — Запрещена трансляция неподобающего контента.
• 4.5 — Запрещено мешать людям разговаривать.""",
			colour=disnake.Colour.gold()
			)
		emb1 = disnake.Embed(
			title = "**Как подключиться к серверу?**",
			description =  f"""**Шаги**

1. 🎫|Вам нужно написать  <@712631530002055169> свой ник в майнкрафт для добавления в white list.
2. 🖱️|Подключитесь по IP: **185.106.92.79:25773**
3. 🎶|Играйе, но стройте базу в не менее 150 блоках от спавна.""",
			colour=disnake.Colour.gold(),
			)
		await self.bot.get_channel(1059760179366854686).send(embed = emb)
		await self.bot.get_channel(1059760179366854686).send(embed = emb1)



def setup(bot: commands.Bot):
	bot.add_cog(rules(bot))