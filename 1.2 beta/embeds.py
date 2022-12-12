import disnake

ban_embed = disnake.Embed(
	title="Пользователь забанен",
	description="Пользователь {member} был забанен по причине: {reason}.",
	colour=0x423189,
	)

black_leaf_embed = disnake.Embed(
	title="Сервер в черном листе",
	description="Сервер или владелец сервера в черном листе.",
	colour=disnake.Colour.red(),
	)

failed_calc_embed = disnake.Embed(
	title="Что-то не так?",
	description="Возможо ты указал запятую вместо точки или в агументе присутствуют пробелы.",
	colour=disnake.Colour.red(),
	)

clear_embed = disnake.Embed(
	title="Сообщения очищены",
	description="Было очищено сообщений: {amount}.",
	colour=0xFFFF00,
	)
failed_clear_embed = disnake.Embed(
	title="Ошибка очистки",
	description="Хм... Это слишком много для меня. Максимум 100.",
	colour=disnake.Colour.red(),
	)

win_guess_embed = disnake.Embed(
		title = 'Вы выиграли!',
		description = 'Поздравляем! Было загадано число {number}.',
		colour = 0xF0C43F,
		)
lose_guess_embed = disnake.Embed(
		title = 'Вы проиграли!',
		description = 'Неверное число. \nБыло загадано число: {number}.',
		colour = disnake.Colour.red(),
		)
failed_guess_embed = disnake.Embed(
		title="Аргменты одинаковы",
		description="\n> Вы указали неправильные аргументы в слэш команде. Аргументы не должны быть больше 20 и не должны быть равны.\nПоменяйте аргументы и попробуйте еще раз.",
		colour= disnake.Colour.red(),
		)

help_embed = disnake.Embed(
		title="Помощь по командам:",
		description="Помощь по командам:\n(Все параметры обязательны)\n\n/ban <Пользователь>\n/calc <Число_1> <Что сделать> <Число_2>\n/clear <кол-во>\n/guess <Число_1> <Число_2>.....\n/info\n/kick <Пользователь>\n/mute <Пользователь>\n/role_by_reaction BETA\n/say <Текст>\n/settings\n/send_private BETA\n/unban",
		color=disnake.Colour.gold(),
	)
help_embed.set_footer(
		text="IvanTopGaming#2635",
		icon_url="https://cdn.discordapp.com/avatars/712631530002055169/e9a8c39a80030e55a5133165237da209.png?size=512"
		)

info_embed = disnake.Embed(
		title = "**Информация о боте**",
		description = "Привет! Я ITG bot. Вот информация обо мне:\n\n**Система:**\nPing: {ping}\nRAM: {RAM}\n\n**О боте:**\nДата создания: {date}\nРазработчик: {dev}\nВерсия: {version}",
		color = disnake.Colour.blue(),
	)
info_embed.set_footer(
	text="IvanTopGaming#2635",
	icon_url="https://cdn.discordapp.com/avatars/712631530002055169/e9a8c39a80030e55a5133165237da209.png?size=512",
	)

kick_embed = disnake.Embed(
	title="Пользователь выгнан",
	description="Пользователь {member} был выгнан по причине: {reason}.",
	colour=0x423189,
	)

mute_embed = disnake.Embed(
	title="Пользователь замьючен",
	description="{member} был замьючен на {time} минут по причине: {reason}.",
	colour=0x423189,
	)

r_b_r_embed = disnake.Embed(
	description="{message}",
	colour=0x00DD7B, #64DA85
	)

say_embed = disnake.Embed(
		description = "{text}",
		color = disnake.Colour.yellow(),
	)

settings_embed = disnake.Embed(
	title = "Настройки", 
	description = "Нажмите на кнопки для настройки", 
	color = disnake.Colour.blue(),
	)
table_settings_embed = disnake.Embed(
	title="Добавлен канал",
	description="Успешно добавлен канал.",
	colour=0x4682B4,
	)
failed_settings_embed = disnake.Embed(
	title="Ошибка записи",
	description="Вы ввели некорректное значение. Возможно, присутствуют буквы или поле пустое. Пожалуйста, повторите запрос.",
	colour=disnake.Colour.red(),
	)
changed_settings_embed = disnake.Embed(
	title="Канал изменен",
	description="Канал лога был успешно изменен.",
	colour=0x4682B4,
	)
off_settings_embed = disnake.Embed(
	title="Уведомления отключены",
	description="Уведомления об участниках отключены.",
	colour=0x006400,
	)
member_join_settings_embed = disnake.Embed(
	title="Новый участник",
	description="{member} присоеденился к серверу.",
	colour=0xD2691E,
	)
member_remove_settings_embed = disnake.Embed(
	title="Участник ушел",
	description="{member} ушел с сервера. Присоеденился {joined_at}",
	colour=0xD2691E,
	)

unban_embed = disnake.Embed(
	title="Пользователь разбанен",
	description="Пользователь {member} был разбанен.",
	colour=0xF5F5DC,
	)
failed_unban_embed = disnake.Embed(
	title='Бан лист пуст',
	description='На сервере нет забаненых участников.',
	colour=disnake.Colour.purple(),
	)
msg_unban_embed = disnake.Embed(
	title='Разбанить участника',
	description='Выберите участника из меню.',
	colour=disnake.Colour.blue()
	)

missing_permissions_embed = disnake.Embed(
	title="Недостаточно прав",
	description="Выдайте боту права администратора для выполнения данной комады.",
	colour=disnake.Colour.red(),
	)
join_embed = disnake.Embed(
	title="Спасибо за добавление на сервер.",
	description="\n🎶 | Благодарю за добавление бота на сервер.\n\nДля просмотра моих команд отправьте **/help**\n\n**Предупреждение! Данная бета верися не стабильна при проблемах обращайтесь на сервер поддержки.**",
	colour=disnake.Colour.gold(),
	)