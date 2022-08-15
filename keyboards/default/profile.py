from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default import keyboard_cancel_uz, keyboard_cancel_ru

profile_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ism familiyani o'zgartirish")
        ],
        keyboard_cancel_uz
    ],
    resize_keyboard=True
)

profile_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить имя фамилию")
        ],
        keyboard_cancel_ru
    ],
    resize_keyboard=True
)
