from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default import keyboard_cancel_uz, keyboard_cancel_ru

cards_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Karta qo'shish")
        ],
        [
            KeyboardButton(text="➖ Kartani o'chirish"),
        ],
        keyboard_cancel_uz
    ],
    resize_keyboard=True
)

cards_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Добавить карту")
        ],
        [
            KeyboardButton(text="➖ Удалить карту"),
        ],
        keyboard_cancel_ru
    ],
    resize_keyboard=True
)
