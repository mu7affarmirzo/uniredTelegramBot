from aiogram.types import Message
from keyboards.default import transactions_uz_button, transactions_ru_button, menu_ru_button, menu_uz_button
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Transaction
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["🔁 O'tkazma", "🔁 Передача"]))
async def show_transactions_menu(message: Message):
    user_id = message.from_user.id
    await Transaction.transaction_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=transactions_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=transactions_uz_button)


@dp.message_handler(Text(equals=["🇺🇿 - 🇺🇿 Mahalliy o'tkazmalar", "🇺🇿 - 🇺🇿 Местные переводы"]),
                    state=Transaction.transaction_menu)
async def process_from_uz_to_uz(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🇺🇿 - 🇷🇺 O'zbekistondan Rossiyaga o'tkazmalar", "🇺🇿 - 🇷🇺 Переводы из Узбекистана в Россию"]),
                    state=Transaction.transaction_menu)
async def process_from_uz_to_ru(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🇷🇺 - 🇺🇿 Rossiyadan O'zbekistonga o'tkazmalar", "🇷🇺 - 🇺🇿 Переводы из России в Узбекистан"]),
                    state=Transaction.transaction_menu)
async def process_from_ru_to_uz(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["⬅️Orqaga", "⬅ Назад"]), state=Transaction.transaction_menu)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=menu_uz_button)

