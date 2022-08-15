from aiogram.dispatcher.filters.state import StatesGroup, State


class Authentication(StatesGroup):
    init = State()
    getting_phone_number = State()
    step_one = State()
    step_two = State()
    login = State()
    register = State()


class Home(StatesGroup):
    home_menu = State()


class Application(StatesGroup):
    application_menu = State()


class Card(StatesGroup):
    card_menu = State()


class Payment(StatesGroup):
    payment_menu = State()


class Transaction(StatesGroup):
    transaction_menu = State()


class History(StatesGroup):
    history_menu = State()


class Profile(StatesGroup):
    profile_menu = State()


class Setting(StatesGroup):
    setting_menu = State()


class AddCard(StatesGroup):
    card_number = State()
    expire = State()
    name = State()
    # is_primary = State()