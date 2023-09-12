# >>> bot stuff
from aiogram import executor
from res.bot.loader import *
from res.bot.handlers import *
from background import keep_alive

class BotApp():
    def __init__(self):
        self.bot = bot
        self.storage = storage
        self.dp = dp

    def start_polling(self):
        print('\033[92m[BOT]\033[0m Bot started')
        keep_alive()
        executor.start_polling(self.dp, skip_updates=True)
    
    def stop_polling(self):
        print('\033[92m[BOT]\033[0m Bot stopped')
        executor.stop_polling(self.dp)