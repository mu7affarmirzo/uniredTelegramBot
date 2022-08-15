import requests
from aiogram.types import Message, ReplyKeyboardRemove

import database
from keyboards.default import cards_uz_button, cards_ru_button, menu_uz_button, menu_ru_button
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Card, AddCard
from data.config import LANG_STORAGE, OTP_TOKEN_STORAGE, API_URL
db = database.DBCommands()


@dp.message_handler(Text(equals=["💳 Kartalarim", "💳 Карты"]))
async def show_cards_manu(message: Message, state: FSMContext):

    user_id = message.from_user.id
    user = await db.get_user(user_id)
    headers = {"Authorization": f"Bearer {user.token}"}
    endpoint = f"{API_URL}/v4/card/card-details"
    r = requests.post(headers=headers, url=endpoint)
    data = r.json()

    await Card.card_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        for card in data['data']:
            await message.answer(f"Card: {card['mask']}\nCard owner: {card['card_owner']}", reply_markup=cards_uz_button)
    elif LANG_STORAGE[user_id] == 'uz':
        for card in data['data']:
            await message.answer(f"Card: {card['mask']}\nCard owner: {card['card_owner']}", reply_markup=cards_uz_button)


@dp.message_handler(Text(equals=["➕ Karta qo'shish", "➕ Добавить карту"]), state=Card.card_menu)
async def add_card(message: Message):
    user_id = message.from_user.id

    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("Введите номер карты: ", reply_markup=ReplyKeyboardRemove())
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("Karta raqamingizni kiriting: ", reply_markup=ReplyKeyboardRemove())
    await AddCard.card_number.set()


@dp.message_handler(state=AddCard.card_number)
async def load_card_number(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = await db.get_user(user_id)
    headers = {"Authorization": f"Bearer {user.token}"}
    endpoint = f"{API_URL}/v4/p2p/get-card-owner-info"
    request_body = {
        "number_token": message.text
    }
    r = requests.post(headers=headers, url=endpoint, json=request_body)
    response_data = r.json()

    async with state.proxy() as data:
        data['card_number'] = message.text
    if LANG_STORAGE[user_id] == 'ru':
        await message.reply(f"Card owner: {response_data['data'][0]['owner']}\nВведите срок действия карты: ", reply_markup=ReplyKeyboardRemove())
    elif LANG_STORAGE[user_id] == 'uz':
        await message.reply(f"Card owner: {response_data['data'][0]['owner']}\nKartaning amal qilish muddatini kiriting: ", reply_markup=ReplyKeyboardRemove())
    await AddCard.next()


@dp.message_handler(Text(equals=["➖ Kartani o'chirish", "➖ Удалить карту"]),
                    state=Card.card_menu)
async def remove_card(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["⬅️Orqaga", "⬅ Назад"]), state=Card.card_menu)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=menu_uz_button)
