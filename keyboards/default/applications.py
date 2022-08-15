from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default import keyboard_cancel_uz, keyboard_cancel_ru

applications_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Unired karta qayta chiqarish"),
        ],
        [
            KeyboardButton(text="Unired kartaga ariza")
        ],
        keyboard_cancel_uz
    ],
    resize_keyboard=True
)

applications_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Перевыпуск карты Unired"),
        ],
        [
            KeyboardButton(text="Подать заявку на карту Unired")
        ],
        keyboard_cancel_ru
    ],
    resize_keyboard=True
)
