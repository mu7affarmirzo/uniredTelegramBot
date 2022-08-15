from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default import keyboard_cancel_uz, keyboard_cancel_ru

history_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text="")
        ],
        keyboard_cancel_uz
    ],
    resize_keyboard=True
)

history_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text="")
        ],
        keyboard_cancel_ru
    ],
    resize_keyboard=True
)
