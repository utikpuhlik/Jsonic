from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.mongo import MongoStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# storage = MongoStorage(host='mongo_db', port=27017, db_name='aiogram_fsm')
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
