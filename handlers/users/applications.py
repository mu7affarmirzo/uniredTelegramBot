from aiogram.types import Message
from keyboards.default import applications_uz_button, applications_ru_button, menu_uz_button, menu_ru_button
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Application
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["🧾 Mening Arizalarim", "🧾 Мои заявки"]))
async def show_applications_menu(message: Message):
    user_id = message.from_user.id
    await Application.application_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=applications_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=applications_uz_button)


@dp.message_handler(Text(equals=["Unired karta qayta chiqarish", "Перевыпуск карты Unired"]),
                    state=Application.application_menu)
async def reissue_card(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["Unired kartaga ariza", "Подать заявку на карту Unired"]),
                    state=Application.application_menu)
async def apply_for_card(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["⬅️Orqaga", "⬅ Назад"]), state=Application.application_menu)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=menu_uz_button)
