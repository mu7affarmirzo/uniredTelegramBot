from aiogram.types import Message
from keyboards.default import payments_uz_button, payments_ru_button, menu_uz_button, menu_ru_button
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Payment
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["💴 To'lovlar", "💴 Платежи"]))
async def show_payments_menu(message: Message):
    user_id = message.from_user.id
    await Payment.payment_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=payments_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=payments_uz_button)


@dp.message_handler(Text(equals=["📱 Uyali aloqa", "📱 Сотовая связь"]),
                    state=Payment.payment_menu)
async def show_list_of_mobile_operators(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["☎ Uy telefoni", "☎️Домашний телефон"]),
                    state=Payment.payment_menu)
async def pay_for_home_phone(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🌐 Internet", "🌐 Интернет"]),
                    state=Payment.payment_menu)
async def show_list_of_internet_providers(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🏢 Xizmatlar", "🏢 Услуги"]),
                    state=Payment.payment_menu)
async def show_list_of_services(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["📺 Televidenie", "📺 Телевидение"]),
                    state=Payment.payment_menu)
async def show_list_of_tv_providers(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🚖 Taksi", "🚖 Такси"]),
                    state=Payment.payment_menu)
async def show_list_of_taxi_providers(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🏳 Xorijiiy xizmatlar", "🏳️ Зарубежные сервисы"]),
                    state=Payment.payment_menu)
async def show_list_of_international_platforms(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🇺🇿 Davlat xizmatlari", "🇺🇿 Государственные услуги"]),
                    state=Payment.payment_menu)
async def show_list_of_government_services(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["💰 Xayriya", "💰 Благотворительность"]),
                    state=Payment.payment_menu)
async def show_list_of_charity_orgs(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["🔌 Komunal to'lovlar", "🔌 Коммунальные платежи"]),
                    state=Payment.payment_menu)
async def show_list_of_utility_services(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["⬅️Orqaga", "⬅ Назад"]), state=Payment.payment_menu)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=menu_uz_button)
