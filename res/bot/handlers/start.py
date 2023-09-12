from res.bot.loader import dp,bot
import aiogram.types as types

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = """
👋 <b>Привіт, я бот для переведення валют з урахуванням комісії steam</b>
""" 
    await bot.send_message(message.chat.id, text,parse_mode='HTML')