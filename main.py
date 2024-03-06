import asyncio
import logging
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from bot import keyboard

from bot.config import TOKEN
from bot.constans import (
    START_STICKER,
    START_TEXT,
    HELP_TEXT
)

# Configure logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


user_id = None
@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    global user_id
    user_id = message.from_user.id
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        cash INTEGER,
        operations TEXT
    )""")
    conn.commit()
    cursor.close()
    conn.close()
    await bot.send_sticker(
        user_id,
        sticker=START_STICKER,
    )
    user(message)
    await bot.send_message(chat_id=message.chat.id, text=START_TEXT.format(message.from_user.first_name), reply_markup=keyboard.main_kb)
    await bot.send_message(chat_id=message.chat.id, text=(f'Ваш id:{user_id}'), reply_markup=keyboard.main_kb)

def user(message: types.Message):
    user_id = message.from_user.id
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT cash FROM users WHERE user_id = {user_id}")
    user = cursor.fetchone()
    if user is None:
        cursor.execute(f"INSERT INTO users (user_id, cash, operations) VALUES ({user_id}, 0, '')")
        conn.commit()
    cursor.close()
    conn.close()

@dp.message(F.text=="Баланс")
async def balance(message: types.Message, cash) -> None:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    result = cursor.fetchone()
    if result:
        cash = result[0]
    cursor.close()
    conn.close()
    await bot.send_message(chat_id=message.chat.id, text=(f"Ваш баланс: {cash}"), reply_markup=keyboard.main_kb)


@dp.message(F.text=="Операції")
async def balance(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text="У розробці ...")


@dp.message(F.text=="Допомога")
async def balance(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text="У розробці ...")


@dp.message(F.text=="Інше")
async def balance(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text="У розробці ...")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
