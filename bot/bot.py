from aiogram import Bot
from aiogram.enums import ParseMode

from bot.config import TOKEN

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)

version = "Beta v1.0"