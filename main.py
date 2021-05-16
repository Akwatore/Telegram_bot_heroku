import os
import telebot
from telebot import types
token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot('token')

keyboard_start = types.InlineKeyboardMarkup()
key_start = types.InlineKeyboardButton(text='Начнём!', callback_data='start_test')
keyboard_start.add(key_start)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я чат-бот сайта Review MMORPG Games и я помогу '
                                      'подобрать тебе игру в жанре мморпг, которая подойдёт именно'
                                      ' для твоего стиля игры.'
                                      'Если ты не знаком с нашим сайтом, то скорее жми по ссылке 😏\n'
                                      'https://reviewmmorpggames.netlify.app/', reply_markup=keyboard_start)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "start_test": #Начало теста
        keyboard = types.InlineKeyboardMarkup()
        key_eu = types.InlineKeyboardButton(text='Западная', callback_data='eu')
        keyboard.add(key_eu)
        key_asia= types.InlineKeyboardButton(text='Восточная', callback_data='asia')
        keyboard.add(key_asia)
        bot.send_message(call.message.chat.id, 'Какая стилистика игры тебе больше нравится?', reply_markup=keyboard)

#Выбор стилистики игры
    if call.data == "eu": #Выбран "Западный" стиль
        keyboard = types.InlineKeyboardMarkup()
        key_typeCamera_1 = types.InlineKeyboardButton(text='От 1-го лица', callback_data='eu_typeCamera_1')
        keyboard.add(key_typeCamera_1)
        key_typeCamera_2 = types.InlineKeyboardButton(text='От 3-го лица', callback_data='eu_typeCamera_2')
        keyboard.add(key_typeCamera_2)
        key_typeCamera_3 = types.InlineKeyboardButton(text='Изометрия', callback_data='eu_typeCamera_3')
        keyboard.add(key_typeCamera_3)
        bot.send_message(call.message.chat.id, 'Какой вид камеры ты больше предпочитаешь?', reply_markup=keyboard)
    elif call.data == "asia": #Выбран "Восточный" стиль
        keyboard = types.InlineKeyboardMarkup()
        key_typeCamera_2 = types.InlineKeyboardButton(text='От 3-го лица', callback_data='asia_typeCamera_2')
        keyboard.add(key_typeCamera_2)
        key_typeCamera_3 = types.InlineKeyboardButton(text='Изометрия', callback_data='asia_typeCamera_3')
        keyboard.add(key_typeCamera_3)
        bot.send_message(call.message.chat.id, 'Какой вид камеры ты больше предпочитаешь?', reply_markup=keyboard)

#Выбран западный стиль
    if call.data == "eu_typeCamera_2": # Западный - От 3-го лица
        keyboard = types.InlineKeyboardMarkup()
        key_target = types.InlineKeyboardButton(text='Таргет', callback_data='etC2_target')
        keyboard.add(key_target)
        key_ntarget = types.InlineKeyboardButton(text='Нон-таргет', callback_data='etC2_ntarget')
        keyboard.add(key_ntarget)
        bot.send_message(call.message.chat.id, 'Таргет или нон-таргет система управления?', reply_markup=keyboard)
    elif call.data == "eu_typeCamera_3": # Западный - Изометрия
        keyboard = types.InlineKeyboardMarkup()
        key_target = types.InlineKeyboardButton(text='Таргет', callback_data='etC3_target')
        keyboard.add(key_target)
        key_ntarget = types.InlineKeyboardButton(text='Нон-таргет', callback_data='etC3_ntarget')
        keyboard.add(key_ntarget)
        bot.send_message(call.message.chat.id, 'Таргет или нон-таргет система управления?', reply_markup=keyboard)



#Западный - камера - управление
    if  call.data == "eu_typeCamera_1": # Западный - От 1-го лица
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='etC1_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='etC1_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)
    if  call.data == "etC2_target": # Западный - От 3-го лица - Таргет
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='etC2t_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='etC2t_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)
    elif call.data == "etC2_ntarget":
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='etC2nt_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='etC2nt_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)
    if  call.data == "etC3_target": # Западный - Изометрия - Таргет
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='etC3t_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='etC3t_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)
    elif call.data == "etC3_ntarget":
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='etC3nt_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='etC3nt_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)



#Западный - камера - управление - ПВЕ/ПВП
    if call.data == "etC1_pve": #От 1-го лица - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='etC1pve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='etC1pve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='etC1pve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "etC1_pvp": #От 1-го лица - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='etC1pvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='etC1pvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='etC1pvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)

    if call.data == "etC2t_pve": #От 3-го лица - Таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='etC2tpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='etC2tpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='etC2tpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "etC2t_pvp": #От 3-го лица - Таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='etC2tpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='etC2tpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='etC2tpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)
    elif call.data == "etC2nt_pve": #От 3-го лица - Нон-таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='etC2ntpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='etC2ntpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='etC2ntpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "etC2nt_pvp": #От 3-го лица - Нон-таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='etC2ntpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='etC2ntpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='etC2ntpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)

    if call.data == "etC3t_pve": #Изометрия - Таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='etC3tpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='etC3tpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='etC3tpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "etC3t_pvp": #Изометрия - Таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='etC3tpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='etC3tpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='etC3tpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)
    elif call.data == "etC3nt_pve": #Изометрия - Нон-таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='etC3ntpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='etC3ntpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='etC3ntpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "etC3nt_pvp": #Изометрия - Нон-таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='etC3ntpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='etC3ntpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='etC3ntpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)





#Западный - От 1-го лица - ПВЕ - список
    if call.data == "etC1pve_raid": #От 1-го лица - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Destiny 2\n''https://reviewmmorpggames.netlify.app/guide/d2guide\n''\n'
                                               'New World\n''https://reviewmmorpggames.netlify.app/guide/nwguide\n')
    elif call.data == "etC1pve_dung": #От 1-го лица - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Destiny 2\n''https://reviewmmorpggames.netlify.app/guide/d2guide\n''\n'
                                               'New World\n''https://reviewmmorpggames.netlify.app/guide/nwguide\n')
    elif call.data == "etC1pve_grind": #От 1-го лица - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Destiny 2\n''https://reviewmmorpggames.netlify.app/guide/d2guide\n''\n'
                                               'New World\n''https://reviewmmorpggames.netlify.app/guide/nwguide\n')
#Западный - От 1-го лица - Нон-таргет - ПВП - список
    if call.data == "etC1pvp_1v1": #От 1-го лица - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Destiny 2\n''https://reviewmmorpggames.netlify.app/guide/d2guide\n''\n'
                                               'New World\n''https://reviewmmorpggames.netlify.app/guide/nwguide\n')
    elif call.data == "etC1pvp_nvn": #От 1-го лица - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Destiny 2\n''https://reviewmmorpggames.netlify.app/guide/d2guide\n''\n'
                                               'New World\n''https://reviewmmorpggames.netlify.app/guide/nwguide\n''\n'
                                               'Reign of Guilds\n''https://reviewmmorpggames.netlify.app/guide/rogguide\n')
    elif call.data == "etC1pvp_gvg": #От 1-го лица - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'New World\n''https://reviewmmorpggames.netlify.app/guide/nwguide\n''\n'
                                               'Reign of Guilds\n''https://reviewmmorpggames.netlify.app/guide/rogguide\n')


#Западный - От 3-го лица - Таргет - ПВЕ - список
    if call.data == "etC2tpve_raid": #От 3-го лица - Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n'
                                               'World of Warcraft\n''https://reviewmmorpggames.netlify.app/guide/wowguide\n')
    elif call.data == "etC2tpve_dung": #От 3-го лица - Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Astellia\n''https://reviewmmorpggames.netlify.app/guide/astelguide\n''\n'
                                               'World of Warcraft\n''https://reviewmmorpggames.netlify.app/guide/wowguide\n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n')
    elif call.data == "etC2tpve_grind": #От 3-го лица - Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Astellia\n''https://reviewmmorpggames.netlify.app/guide/astelguide\n''\n'
                                               'World of Warcraft\n''https://reviewmmorpggames.netlify.app/guide/wowguide\n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n')
#Западный - От 3-го лица - Таргет - ПВП - список
    if call.data == "etC2tpvp_1v1": #От 3-го лица - Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n'
                                               'World of Warcraft\n''https://reviewmmorpggames.netlify.app/guide/wowguide\n')
    elif call.data == "etC2tpvp_nvn": #От 3-го лица - Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Astellia\n''https://reviewmmorpggames.netlify.app/guide/astelguide\n''\n'
                                               'World of Warcraft\n''https://reviewmmorpggames.netlify.app/guide/wowguide\n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n')
    elif call.data == "etC2tpvp_gvg": #От 3-го лица - Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n'
                                               'World of Warcraft\n''https://reviewmmorpggames.netlify.app/guide/wowguide\n')


#Западный - От 3-го лица - Нон-таргет - ПВЕ - список
    if call.data == "etC2ntpve_raid": #От 3-го лица - Нон-Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Tera\n''https://reviewmmorpggames.netlify.app/guide/teraguide\n''\n')
    elif call.data == "etC2ntpve_dung": #От 3-го лица - Нон-Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n''\n'
                                               'Tera\n''https://reviewmmorpggames.netlify.app/guide/teraguide\n')
    elif call.data == "etC2ntpve_grind": #От 3-го лица - Нон-Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n''\n'
                                               'Tera\n''https://reviewmmorpggames.netlify.app/guide/teraguide\n')
#Западный - От 3-го лица - Нон-таргет - ПВП - список
    if call.data == "etC2ntpvp_1v1": #От 3-го лица - Нон-Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n''\n')
    elif call.data == "etC2ntpvp_nvn": #От 3-го лица - Нон-Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Tera\n''https://reviewmmorpggames.netlify.app/guide/teraguide\n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n')
    elif call.data == "etC2ntpvp_gvg": #От 3-го лица - Нон-Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n''\n'
                                               'Tera\n''https://reviewmmorpggames.netlify.app/guide/teraguide\n')


#Западный - Изометрия - Таргет - ПВЕ - список
    if call.data == "etC3tpve_raid": #Изометрия - Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n')
    elif call.data == "etC3tpve_dung": #Изометрия - Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
    elif call.data == "etC3tpve_grind": #Изометрия - Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
#Западный - Изометрия - Таргет - ПВП - список
    if call.data == "etC3tpvp_1v1": #Изометрия - Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Last Epoch\n''https://reviewmmorpggames.netlify.app/guide/leguide\n''\n')
    elif call.data == "etC3tpvp_nvn": #Изометрия - Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n')
    elif call.data == "etC3tpvp_gvg": #Изометрия - Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n''\n')


#Западный - Изометрия - Нон-таргет - ПВЕ - список
    if call.data == "etC3ntpve_raid": #Изометрия - Нон-Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n')
    elif call.data == "etC3ntpve_dung": #Изометрия - Нон-Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
    elif call.data == "etC3ntpve_grind": #Изометрия - Нон-Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
#Западный - Изометрия - Нон-таргет - ПВП - список
    if call.data == "etC3ntpvp_1v1": #Изометрия - Нон-Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Last Epoch\n''https://reviewmmorpggames.netlify.app/guide/leguide\n''\n')
    elif call.data == "etC3ntpvp_nvn": #Изометрия - Нон-Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n')
    elif call.data == "etC3ntpvp_gvg": #Изометрия - Нон-Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n''\n')








#Выбран восточный стиль
    if call.data == "asia_typeCamera_2": # Восточный - От 3-го лица
        keyboard = types.InlineKeyboardMarkup()
        key_target = types.InlineKeyboardButton(text='Таргет', callback_data='atC2_target')
        keyboard.add(key_target)
        key_ntarget = types.InlineKeyboardButton(text='Нон-таргет', callback_data='atC2_ntarget')
        keyboard.add(key_ntarget)
        bot.send_message(call.message.chat.id, 'Таргет или нон-таргет система управления?', reply_markup=keyboard)
    elif call.data == "asia_typeCamera_3": # Восточный - Изометрия
        keyboard = types.InlineKeyboardMarkup()
        key_target = types.InlineKeyboardButton(text='Таргет', callback_data='atC3_target')
        keyboard.add(key_target)
        key_ntarget = types.InlineKeyboardButton(text='Нон-таргет', callback_data='atC3_ntarget')
        keyboard.add(key_ntarget)
        bot.send_message(call.message.chat.id, 'Таргет или нон-таргет система управления?', reply_markup=keyboard)


#Восточный - камера - управление
    if  call.data == "atC2_target": # Восточный - От 3-го лица - Таргет
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='atC2t_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='atC2t_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)
    elif call.data == "atC2_ntarget":
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='atC2nt_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='atC2nt_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)
    if  call.data == "atC3_target": # Восточный - Изометрия - Таргет
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='atC3t_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='atC3t_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)
    elif call.data == "atC3_ntarget":
        keyboard = types.InlineKeyboardMarkup()
        key_pve = types.InlineKeyboardButton(text='ПВЕ', callback_data='atC3nt_pve')
        keyboard.add(key_pve)
        key_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='atC3nt_pvp')
        keyboard.add(key_pvp)
        bot.send_message(call.message.chat.id, 'ПВЕ или ПВП?', reply_markup=keyboard)


#Восточный - камера - управление - ПВЕ/ПВП
    if call.data == "atC2t_pve": #От 3-го лица - Таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='atC2tpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='atC2tpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='atC2tpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "atC2t_pvp": #От 3-го лица - Таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='atC2tpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='atC2tpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='atC2tpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)
    elif call.data == "atC2nt_pve": #От 3-го лица - Нон-таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='atC2ntpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='atC2ntpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='atC2ntpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "atC2nt_pvp": #От 3-го лица - Нон-таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='atC2ntpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='atC2ntpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='atC2ntpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)

    if call.data == "atC3t_pve": #Изометрия - Таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='atC3tpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='atC3tpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='atC3tpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "atC3t_pvp": #Изометрия - Таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='atC3tpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='atC3tpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='atC3tpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)
    elif call.data == "atC3nt_pve": #Изометрия - Нон-таргет - ПВЕ
        keyboard = types.InlineKeyboardMarkup()
        key_raid = types.InlineKeyboardButton(text='Рейды', callback_data='atC3ntpve_raid')
        keyboard.add(key_raid)
        key_dung = types.InlineKeyboardButton(text='Данжи', callback_data='atC3ntpve_dung')
        keyboard.add(key_dung)
        key_grind = types.InlineKeyboardButton(text='Гринд мобов', callback_data='atC3ntpve_grind')
        keyboard.add(key_grind)
        bot.send_message(call.message.chat.id, 'Чем тебе больше нравится заниматься в игре?', reply_markup=keyboard)
    elif call.data == "atC3nt_pvp": #Изометрия - Нон-таргет - ПВП
        keyboard = types.InlineKeyboardMarkup()
        key_1v1 = types.InlineKeyboardButton(text='1 vs 1', callback_data='atC3ntpvp_1v1')
        keyboard.add(key_1v1)
        key_nvn = types.InlineKeyboardButton(text='N vs N (несколько игроков против нескольких)', callback_data='atC3ntpvp_nvn')
        keyboard.add(key_nvn)
        key_gvg = types.InlineKeyboardButton(text='Битва гильдий', callback_data='atC3ntpvp_gvg')
        keyboard.add(key_gvg)
        bot.send_message(call.message.chat.id, 'Какой формат ПВП тебе предпочтительнее?', reply_markup=keyboard)





#Восточный - От 3-го лица - Таргет - ПВЕ - список
    if call.data == "atC2tpve_raid": #От 3-го лица - Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n'
                                               'Revelation Online\n''https://reviewmmorpggames.netlify.app/guide/revguide\n')
    elif call.data == "atC2tpve_dung": #От 3-го лица - Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n'
                                               'Revelation Online\n''https://reviewmmorpggames.netlify.app/guide/revguide\n')
    elif call.data == "atC2tpve_grind": #От 3-го лица - Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n')
#Восточный - От 3-го лица - Таргет - ПВП - список
    if call.data == "atC2tpvp_1v1": #От 3-го лица - Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n')
    elif call.data == "atC2tpvp_nvn": #От 3-го лица - Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n'
                                               'Revelation Online\n''https://reviewmmorpggames.netlify.app/guide/revguide\n')
    elif call.data == "atC2tpvp_gvg": #От 3-го лица - Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Aion\n''https://reviewmmorpggames.netlify.app/guide/aionguide\n''\n')


#Восточный - От 3-го лица - Нон-таргет - ПВЕ - список
    if call.data == "atC2ntpve_raid": #От 3-го лица - Нон-Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Revelation Online\n''https://reviewmmorpggames.netlify.app/guide/revguide\n''\n'
                                               'Blade and Soul\n''https://reviewmmorpggames.netlify.app/guide/bnsguide\n')
    elif call.data == "atC2ntpve_dung": #От 3-го лица - Нон-Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Blade and Soul \n''https://reviewmmorpggames.netlify.app/guide/bnsguide\n''\n'
                                               'Revelation Online\n''https://reviewmmorpggames.netlify.app/guide/revguide\n')
    elif call.data == "atC2ntpve_grind": #От 3-го лица - Нон-Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n''\n')
#Восточный - От 3-го лица - Нон-таргет - ПВП - список
    if call.data == "atC2ntpvp_1v1": #От 3-го лица - Нон-Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n''\n'
                                               'Blade and Soul\n''https://reviewmmorpggames.netlify.app/guide/bnsguide\n')
    elif call.data == "atC2ntpvp_nvn": #От 3-го лица - Нон-Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Blade and Soul\n''https://reviewmmorpggames.netlify.app/guide/bnsguide\n''\n'
                                               'Revelation Online\n''https://reviewmmorpggames.netlify.app/guide/revguide\n')
    elif call.data == "atC2ntpvp_gvg": #От 3-го лица - Нон-Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Black Desert\n''https://reviewmmorpggames.netlify.app/guide/bdoguide\n''\n'
                                               'Blade and Soul\n''https://reviewmmorpggames.netlify.app/guide/bnsguide\n')


#Восточный - Изометрия - Таргет - ПВЕ - список
    if call.data == "atC3tpve_raid": #Изометрия - Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n')
    elif call.data == "atC3tpve_dung": #Изометрия - Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
    elif call.data == "atC3tpve_grind": #Изометрия - Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
#Восточный - Изометрия - Таргет - ПВП - список
    if call.data == "atC3tpvp_1v1": #Изометрия - Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Royal Quest\n''https://reviewmmorpggames.netlify.app/guide/rqguide\n''\n')
    elif call.data == "atC3tpvp_nvn": #Изометрия - Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Royal Quest\n''https://reviewmmorpggames.netlify.app/guide/rqguide\n')
    elif call.data == "atC3tpvp_gvg": #Изометрия - Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Royal Quest\n''https://reviewmmorpggames.netlify.app/guide/rqguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')


#Восточный - Изометрия - Нон-таргет - ПВЕ - список
    if call.data == "atC3ntpve_raid": #Изометрия - Нон-Таргет - ПВЕ - рейды - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n')
    elif call.data == "atC3ntpve_dung": #Изометрия - Нон-Таргет - ПВЕ - данжи - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
    elif call.data == "atC3ntpve_grind": #Изометрия - Нон-Таргет - ПВЕ - гринд - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')
#Восточный - Изометрия - Нон-таргет - ПВП - список
    if call.data == "atC3ntpvp_1v1": #Изометрия - Нон-Таргет - ПВП - 1х1 - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Royal Quest\n''https://reviewmmorpggames.netlify.app/guide/rqguide\n''\n')
    elif call.data == "atC3ntpvp_nvn": #Изометрия - Нон-Таргет - ПВП - массовые - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Lost Ark\n''https://reviewmmorpggames.netlify.app/guide/laguide\n''\n'
                                               'Royal Quest\n''https://reviewmmorpggames.netlify.app/guide/rqguide\n')
    elif call.data == "atC3ntpvp_gvg": #Изометрия - Нон-Таргет - ПВП - гильдии - список
        bot.send_message(call.message.chat.id, 'Со всеми играми в жанре MMORPG ты можешь ознакомиться '
                                               'на нашем сайте Review MMORPG Games. Там ты найдёшь краткую информацию '
                                               'о играх, о доступных локализациях и ссылки на официальные сайты. '
                                               'А также всевозможные гайды и подсказки 😉'
                                               'https://reviewmmorpggames.netlify.app/ \n''\n'
                                               'А эти игры подобраны специально для тебя: \n''\n'
                                               'Royal Quest\n''https://reviewmmorpggames.netlify.app/guide/rqguide\n''\n'
                                               'Ragnarok Online\n''https://reviewmmorpggames.netlify.app/guide/roguide\n')

bot.polling()
