from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default import keyboard_cancel_uz, keyboard_cancel_ru

settings_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇿🇺 Tilni o'zgartirish")
        ],
        [
            KeyboardButton(text="🔐 PIN-kodni o'zgartirish"),
        ],
        keyboard_cancel_uz
    ],
    resize_keyboard=True
)

settings_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇿🇺 Изменение языка")
        ],
        [
            KeyboardButton(text="🔐 Изменить PIN-код"),
        ],
        keyboard_cancel_ru
    ],
    resize_keyboard=True
)
