from packages.bot.loader import dp,bot
from aiogram import types

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    text = """
<b>Доступні команди:</b>
/start - Почати роботу з ботом
/help - Допомога

<b>Як перевести валюту?</b>
<b>Формат</b>: <i>uan usd 38 100</i>
    uan - валюта з якої переводимо
    usd - валюта в яку переводимо
    38 - курс валюти uan до usd
    100 - сума яку переводимо
"""

    await bot.send_message(message.chat.id, text,parse_mode='HTML')
