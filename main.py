import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from bot import keyboard

from bot.config import TOKEN
from bot.constans import (
    START_STICKER,
    START_TEXT,
    HELP_TEXT
)


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    user_id = message.from_user.id
    await bot.send_sticker(
        user_id,
        sticker=START_STICKER,
    )
    await bot.send_message(chat_id=message.chat.id, text=START_TEXT.format(message.from_user.first_name), reply_markup=keyboard.main_kb)


@dp.message(F.text=="Баланс")
async def balance(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text="Ваш баланс: 0")


@dp.message(F.text=="Операції")
async def balance(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text="У розробці ...")


@dp.message(F.text=="Допомога")
async def balance(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text="Якщо вам потрібна моя допомога: @zmiiovskyi", reply_markup=keyboard.main_kb)


@dp.message(F.text=="Інше")
async def balance(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id, text="У розробці ...")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
