from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from keyboards.default import *
from loader import dp
import database
from data.config import LANG_STORAGE
from states import Authentication

db = database.DBCommands()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await db.get_user(user_id)
    await state.reset_state()
    if user is not None:
        if user.language == 'ru':
            LANG_STORAGE[user_id] = 'ru'
        elif user.language == 'uz':
            LANG_STORAGE[user_id] = 'uz'
        await Authentication.getting_phone_number.set()
    else:
        await db.add_new_user()
        await message.answer("🌍 Язык/Til:", reply_markup=language_button)
        await Authentication.init.set()


@dp.message_handler(Text(equals=["🏠 Asosiy sahifaga", "🏠 На главную"]), state="*")
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)


@dp.message_handler(commands=['stop'], state='*')
async def stop(message: types.Message, state: FSMContext):
    await state.reset_state()
    user_id = message.from_user.id
    try:
        del LANG_STORAGE[user_id]
    except KeyError:
        pass
