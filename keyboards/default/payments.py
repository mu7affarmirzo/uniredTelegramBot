from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default import keyboard_cancel_uz, keyboard_cancel_ru

payments_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Uyali aloqa"),
            KeyboardButton(text="☎ Uy telefoni"),
        ],
        [
            KeyboardButton(text="🌐 Internet"),
            KeyboardButton(text="🏢 Xizmatlar"),
        ],
        [
            KeyboardButton(text="📺 Televidenie"),
            KeyboardButton(text="🚖 Taksi"),
        ],
        [
            KeyboardButton(text="🏳 Xorijiiy xizmatlar"),
            KeyboardButton(text="🇺🇿 Davlat xizmatlari"),
        ],
        [
            KeyboardButton(text="💰 Xayriya"),
            KeyboardButton(text="🔌 Komunal to'lovlar"),
        ],
        keyboard_cancel_uz
    ],
    resize_keyboard=True
)

payments_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Сотовая связь"),
            KeyboardButton(text="☎️Домашний телефон"),
        ],
        [
            KeyboardButton(text="🌐 Интернет"),
            KeyboardButton(text="🏢 Услуги"),
        ],
        [
            KeyboardButton(text="📺 Телевидение"),
            KeyboardButton(text="🚖 Такси"),
        ],
        [
            KeyboardButton(text="🏳️ Зарубежные сервисы"),
            KeyboardButton(text="🇺🇿 Государственные услуги"),
        ],
        [
            KeyboardButton(text="💰 Благотворительность"),
            KeyboardButton(text="🔌 Коммунальные платежи"),
        ],
        keyboard_cancel_ru
    ],
    resize_keyboard=True
)
