import requests
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default import menu_ru_button, menu_uz_button
from loader import dp
import database
from states import Authentication, Home
from data.config import LANG_STORAGE, API_URL, OTP_TOKEN_STORAGE

db = database.DBCommands()


async def error_happened(message, state, user_id):
    if LANG_STORAGE[user_id] == 'ru':
        await message.reply("Извините, что-то пошло не так! (/start)")
        await state.reset_state()
    elif LANG_STORAGE[user_id] == 'uz':
        await message.reply("Kechirasiz, nimadir noto'g'ri ketdi! (/start)")
        await state.reset_state()
        await state.finish()


@dp.message_handler(Text(equals=["🇷🇺 Русский", "🇺🇿 O'zbek"]), state=Authentication.init)
async def set_language(message: Message):
    user_id = message.from_user.id
    if message.text == "🇷🇺 Русский":
        LANG_STORAGE[user_id] = 'ru'
        await db.set_language('ru')
    elif message.text == "🇺🇿 O'zbek":
        LANG_STORAGE[user_id] = 'uz'
        await db.set_language('uz')
    await Authentication.getting_phone_number.set()


@dp.message_handler(state=Authentication.getting_phone_number)
async def get_phone_number(message: Message):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="мой номер ☎", request_contact=True))
        await message.answer("Отправить мой номер боту:", reply_markup=keyboard)
    elif LANG_STORAGE[user_id] == 'uz':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Mening raqamim", request_contact=True))
        await message.answer("Mening raqamimni botga yuboring:", reply_markup=keyboard)
    await Authentication.step_one.set()


@dp.message_handler(state=Authentication.step_one, content_types=types.ContentTypes.CONTACT)
async def process_step_one(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    mobile = message.contact.phone_number.replace('+', '')
    await db.set_phone_number(mobile)
    lang = LANG_STORAGE[user_id]
    request_body = {
        "mobile": mobile,
        "lang": lang
    }
    r = requests.post(f"{API_URL}/v4/auth/step-1", json=request_body)
    if r.status_code == 200 and r.json()["status"]:
        data = r.json()
        OTP_TOKEN_STORAGE[user_id] = data["data"][0]["otp"]
        user_id = message.from_user.id
        if LANG_STORAGE[user_id] == 'ru':
            await message.reply("Tasdiqlash kodini kiriting:")
        elif LANG_STORAGE[user_id] == 'uz':
            await message.reply("Введите код подтверждения:")
        await Authentication.step_two.set()
    else:
        await error_happened(message, state, user_id)


@dp.message_handler(state=Authentication.step_two)
async def process_step_two(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data["otp"] = message.text
        request_body = {
            "otp_token": OTP_TOKEN_STORAGE[user_id],
            "otp": data["otp"],
            "forgot": 0
        }
        r = requests.post(f"{API_URL}/v4/auth/step-2", json=request_body)
        if r.status_code == 200 and r.json()["status"]:
            data = r.json()
            is_registered = data["data"][0]["is_registered"]
            if LANG_STORAGE[user_id] == 'ru':
                await message.reply("Пожалуйста введите пароль:")
            elif LANG_STORAGE[user_id] == 'uz':
                await message.reply("Iltimos, parolni kiriting:")
            if is_registered:
                if LANG_STORAGE[user_id] == 'ru':
                    await message.reply("Пожалуйста введите пароль для авторизоваться:")
                elif LANG_STORAGE[user_id] == 'uz':
                    await message.reply("Iltimos, tizimga kirish uchun parolni kiriting:")
                await Authentication.login.set()
            else:
                if LANG_STORAGE[user_id] == 'ru':
                    await message.reply("Пожалуйста введите пароль для регистрация:")
                elif LANG_STORAGE[user_id] == 'uz':
                    await message.reply("Iltimos, ro'yxatdan o'tish uchun parolni kiriting:")
                await Authentication.register.set()
        else:
            await error_happened(message, state, user_id)


@dp.message_handler(state=Authentication.login)
async def login(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data["password"] = message.text
        request_body = {
            "otp_token": OTP_TOKEN_STORAGE[user_id],
            "password": data["password"],
            "details": {
                "ip": "no",
                "imei": "no",
                "mac": "no",
                "name": "no",
                "lat": "no",
                "long": "no",
                "firebase_reg_id": "no",
                "uuid": "no",
                "version": "no"
            }
        }
        endpoint = f"{API_URL}/v4/auth/login"
        r = requests.post(endpoint, json=request_body)
        if r.status_code == 200 and r.json()["status"]:
            data = r.json()
            access_token = data["data"][0]["access_token"]
            await db.set_token(access_token)
            if LANG_STORAGE[user_id] == 'ru':
                await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
            elif LANG_STORAGE[user_id] == 'uz':
                await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)
        else:
            await error_happened(message, state, user_id)


@dp.message_handler(state=Authentication.register)
async def register(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await db.get_user(user_id)
    if user is not None:
        async with state.proxy() as data:
            data["password"] = message.text
            request_body = {
                "otp_token": OTP_TOKEN_STORAGE[user_id],
                "name": user.full_name,
                "last_name": "",
                "mobile": user.phone_number,
                "email": "",
                "password": data["password"],
                "details": {
                    "ip": "no",
                    "imei": "no",
                    "mac": "no",
                    "name": "no",
                    "lat": "no",
                    "long": "no",
                    "firebase_reg_id": "no",
                    "uuid": "no",
                    "version": "no"
                }
            }
            endpoint = f"{API_URL}/v4/auth/register"
            r = requests.post(endpoint, json=request_body)
            if r.status_code == 200 and r.json()["status"]:
                data = r.json()
                access_token = data["data"][0]["access_token"]
                await db.set_token(access_token)
                if LANG_STORAGE[user_id] == 'ru':
                    await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
                elif LANG_STORAGE[user_id] == 'uz':
                    await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)
            else:
                await error_happened(message, state, user_id)
    else:
        await error_happened(message, state, user_id)
