import psycopg
from psycopg.rows import dict_row
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def get_connection():
    return psycopg.connect(DATABASE_URI, row_factory=dict_row)