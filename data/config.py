import os
from dotenv import load_dotenv

load_dotenv()
LANG_STORAGE = {}
OTP_TOKEN_STORAGE = {}
BOT_TOKEN = str(os.getenv("TG_API_TOKEN"))
admins = [
]
POSTGRES_USER = str(os.getenv("POSTGRES_USER"))
POSTGRES_DB = str(os.getenv("POSTGRES_DB"))
POSTGRES_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
DATABASE_URL = str(os.getenv("DATABASE_URL"))
API_URL = str(os.getenv("API_URL"))
