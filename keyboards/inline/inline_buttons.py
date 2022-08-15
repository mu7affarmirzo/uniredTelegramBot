from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


demo_uz = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Demo", callback_data="demo",
                                 url="")
        ],
    ]
)