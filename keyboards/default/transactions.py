from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default import keyboard_cancel_uz, keyboard_cancel_ru

transactions_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 - 🇺🇿 Mahalliy o'tkazmalar")
        ],
        [
            KeyboardButton(text="🇺🇿 - 🇷🇺 O'zbekistondan Rossiyaga o'tkazmalar")
        ],
        [
            KeyboardButton(text="🇷🇺 - 🇺🇿 Rossiyadan O'zbekistonga o'tkazmalar")
        ],
        keyboard_cancel_uz
    ],
    resize_keyboard=True
)

transactions_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 - 🇺🇿 Местные переводы")
        ],
        [
            KeyboardButton(text="🇺🇿 - 🇷🇺 Переводы из Узбекистана в Россию")
        ],
        [
            KeyboardButton(text="🇷🇺 - 🇺🇿 Переводы из России в Узбекистан")
        ],
        keyboard_cancel_ru
    ],
    resize_keyboard=True
)
