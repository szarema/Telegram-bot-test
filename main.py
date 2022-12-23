from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
TOKEN_API = "5659392835:AAEQDstlwF2rPtTtLG6_EwsAaGp6xxZEvv4"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text="/matan")
b2 = KeyboardButton(text="/statistics")
b3 = KeyboardButton(text="/ipr")
b4 = KeyboardButton(text="/caos")
b5 = KeyboardButton(text="/evaluation")
kb.add(b1, b2)
kb.add(b3, b4, b5)

ikb = InlineKeyboardMarkup(row_width=2)
ib = InlineKeyboardButton(text="Перейти", url="http://wiki.cs.hse.ru/Wiki_ФКН")
ikb.add(ib)

HELP_COMMAND = """
1. <b> /start </b> - приветствие
2. <b> /help </b> - помощь 
3. <b>/count </b> - количество вызовов
4. <b> /contacts </b> - контакты преподавателей
5. <b> /matan </b> - материалы по математическому анализу
6. <b> /statistics </b> - материалы по теории вероятностей 
7. <b> /ipr </b> - материалы по ИПР
8. <b> /caos </b> - материалы по АКОС
9. <b> /site </b> - вики страница ФКН
10. <b> /evaluation </b> - оценивание бота 
"""

count = 0

# Приветствие
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=" <b>Здравствуйте! </b> \n <em> Я бот для 2-ого курса ФКН ПМИ для быстрого"
                              " нахождения материалов. Чем могу помочь? </em>", parse_mode="HTML",
                         reply_markup=kb)
    global count
    count += 1

# Помощь
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode="HTML")
    global count
    count += 1

# Количество вызовов
@dp.message_handler(commands=['count'])
async def check_count(message: types.Message):
    global count
    await message.answer(f'Количество вызовов:{count}')
    count += 1

# Высылает изображение с контактами лекторов
@dp.message_handler(commands=['contacts'])
async def send_image(message: types.Message):
    await message.answer(text="✅ <b> Высылаю контакты преподавателей </b>", parse_mode="HTML")
    photo = open('/Users/zarema/Desktop/telegram-bot-test/contact.png', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    global count
    count += 1

# Математический анализ (текст + документ + кнопка)
@dp.message_handler(commands=['matan'])
async def help_command(message: types.Message):
    await message.answer(text="✅ <b> Высылаю лекции по математическому анализу </b>", parse_mode="HTML")
    doc = open('/Users/zarema/Desktop/telegram-bot-test/MA_2_lec1.pdf', 'rb')
    await bot.send_document(chat_id=message.chat.id, document=doc)
    global count
    count += 1

# Теория вероятностей (текст + документ + кнопка)
@dp.message_handler(commands=['statistics'])
async def help_command(message: types.Message):
    await message.answer(text="✅ <b> Высылаю лекции по теории вероятностей </b>", parse_mode="HTML")
    doc = open('/Users/zarema/Desktop/telegram-bot-test/conspects.pdf', 'rb')
    await bot.send_document(chat_id=message.chat.id, document=doc)
    global count
    count += 1

# ИПР (текст + ссылка + кнопка)
@dp.message_handler(commands=['ipr'])
async def help_command(message: types.Message):
    await message.answer(text="✅ <b> Для просмотра материалов по ИПР перейдите по ссылке </b> \n"
                              "http://wiki.cs.hse.ru/Инструменты_промышленной_разработки_2022/2023", parse_mode="HTML")
    global count
    count += 1

# Акос (текст + ссылка + кнопка)
@dp.message_handler(commands=['caos'])
async def help_command(message: types.Message):
    await message.answer(text="✅ <b> Для просмотра материалов по АКОС перейдите по ссылке </b> \n"
                              "http://wiki.cs.hse.ru/CAOS-2022", parse_mode="HTML")
    global count
    count += 1

# Сайт (текст + ссылка в кнопке в сообщениях)
@dp.message_handler(commands=['site'])
async def help_command(message: types.Message):
    await message.answer(text="✅ <b> Просмотр вики страницы </b>", parse_mode="HTML", reply_markup=ikb)
    global count
    count += 1

# Оценка бота

@dp.message_handler(commands=['evaluation'])
async def evalution_command(message: types.Message):
    ikb1 = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='❤️', callback_data='like')
    ib2 = InlineKeyboardButton(text='💔', callback_data='dislike')
    ikb1.add(ib1, ib2)
    photo = open('/Users/zarema/Desktop/telegram-bot-test/mark.jpeg', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Как Вам бот?", reply_markup=ikb1)

# Оценка бота - для callback_data
@dp.callback_query_handler()
async def evalution_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Спасибо за положительную оценку!')
    await callback.answer(text=':(')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
