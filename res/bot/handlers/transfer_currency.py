from res.bot.loader import dp,bot
from aiogram.types import Message
import re

@dp.message_handler(lambda message: re.match(get_regex_transfer(), message.text))
async def transfer_currency(message: Message):
    first_name, second_name, exchange_rate, amount = message.text.split()

    result_exchange_rate = float(amount)/ float(exchange_rate) 
    
    steam_commision = 13
    result = result_exchange_rate/(1-(steam_commision/100))

    text = f"""
💵 <b>{amount} {first_name}</b> to 💵 <b>{second_name}</b> 
💹 <b>exchange result</b> = <i>{round(result_exchange_rate,3)} {second_name}</i>
💳 <b>with steam commison</b> <i>{steam_commision}%</i> = <i>{round(result,3)}</i> <b>{second_name}</b>💵
    """

    await bot.send_message(message.chat.id,text,parse_mode='HTML')

def get_regex_transfer():
    return r'^\w+\s\w+\s\d+\s\d+$'
