from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Баланс"),
            KeyboardButton(text="Операції")
        ],
        [
            KeyboardButton(text="Допомога"),
            KeyboardButton(text="Інше")
        ]
    ],
    resize_keyboard=True,
    selective=True
)



