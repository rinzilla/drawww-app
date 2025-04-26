import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '7575940912:AAGZadQi6Ua0T-WwL6uL4ZZY0trR_DTbnY8'  # <-- сюда вставь токен от @BotFather

# СЮДА вставь ссылку на твою залитую рисовалку
WEBAPP_URL = 'https://drawww-app.vercel.app'  # например: https://my-draw-app.vercel.app/

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="✏️ Нарисовать", web_app=WebAppInfo(url=WEBAPP_URL)))

    await message.answer("Нажми кнопку ниже, чтобы нарисовать картинку:", reply_markup=markup)

# Приём данных от WebApp (рисунка)
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_data_handler(message: types.Message):
    data = message.web_app_data.data  # Здесь base64 код рисунка
    await message.answer_photo(photo=data, caption="Вот твой рисунок! 🎨")

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)