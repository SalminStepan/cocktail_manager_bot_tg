import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

raw_admin_ids = os.getenv("ADMIN_IDS")
if not raw_admin_ids:
    ADMIN_IDS = set()
else:
    parts = raw_admin_ids.split(",")
    cleaned_parts = [x.strip() for x in parts]
    ADMIN_IDS = set(int(x) for x in cleaned_parts if x)
