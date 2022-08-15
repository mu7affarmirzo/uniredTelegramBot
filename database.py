from aiogram import types
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    Text
)
from sqlalchemy import sql

from data.config import DATABASE_URL

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    language = Column(String(2))
    full_name = Column(String(100))
    username = Column(String(50))
    phone_number = Column(String(50), nullable=True)
    token = Column(Text, nullable=True)
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.full_name, self.username)


class DBCommands:

    def __init__(self):
        pass

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self, phone_number=None, token=None):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name
        new_user.phone_number = phone_number
        new_user.token = token

        await new_user.create()
        return new_user

    async def set_language(self, language):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(language=language).apply()

    async def set_phone_number(self, phone_number):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(phone_number=phone_number).apply()

    async def set_token(self, token):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(token=token).apply()


async def create_db():
    await db.set_bind(DATABASE_URL)

    # Create tables
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()
