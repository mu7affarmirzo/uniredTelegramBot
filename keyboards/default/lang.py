from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="🇷🇺 Русский"),
        KeyboardButton(text="🇺🇿 O'zbek")

     ],
    ],
    resize_keyboard=True
)
