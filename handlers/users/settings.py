from aiogram.types import Message
from keyboards.default import settings_uz_button, settings_ru_button, menu_ru_button, menu_uz_button
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Setting
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["⚙ Sozlamalar", "⚙ Настройки"]))
async def show_settings_menu(message: Message):
    user_id = message.from_user.id
    await Setting.setting_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=settings_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=settings_uz_button)


@dp.message_handler(Text(equals=["🇿🇺 Tilni o'zgartirish", "🇿🇺 Изменение языка"]),
                    state=Setting.setting_menu)
async def change_language(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🔐 PIN-kodni o'zgartirish", "🔐 Изменить PIN-код"]),
                    state=Setting.setting_menu)
async def change_pin(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["⬅️Orqaga", "⬅ Назад"]), state=Setting.setting_menu)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=menu_uz_button)
