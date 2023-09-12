from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from packages.utils.env import get_env_variable

# Задайте дані проксі
proxy_host = "45.142.252.131"
proxy_port = 3000
proxy_username = "QKP1qI"
proxy_password = "aRCB7dfexC"

# Створіть об'єкт проксі
proxy = f"https://{proxy_host}:{proxy_port}/"

# Створіть об'єкт бота з проксі
bot = Bot(token=get_env_variable("TOKEN"), parse_mode=types.ParseMode.HTML, proxy=proxy)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
