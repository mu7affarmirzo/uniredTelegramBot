from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧾 Mening Arizalarim"),

        ],
        [
            KeyboardButton(text="💳 Kartalarim"),
            KeyboardButton(text="💴 To'lovlar")

        ],
        [
            KeyboardButton(text="🔁 O'tkazma"),
            KeyboardButton(text="📜 To'lovlar Tarixi")

        ],
        [
            KeyboardButton(text="🟦 Profil"),
            KeyboardButton(text="⚙ Sozlamalar")

        ],
    ],
    resize_keyboard=True
)

menu_ru_button = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🧾 Мои заявки"),

        ],
        [
            KeyboardButton(text="💳 Карты"),
            KeyboardButton(text="💴 Платежи")

        ],
        [
            KeyboardButton(text="🔁 Передача"),
            KeyboardButton(text="📜 История платежей")

        ],
        [
            KeyboardButton(text="🟦 Профиль"),
            KeyboardButton(text="⚙ Настройки"),

        ],
    ],
    resize_keyboard=True
)
