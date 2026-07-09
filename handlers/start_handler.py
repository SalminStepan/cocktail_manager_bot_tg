# Этот файл содержит обработчик команды /start.
# Он отвечает за первое сообщение пользователю и объясняет базовые возможности read-only бота.
import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command
from services.analytics_service import log_bot_event


start_router = Router()
# Отправляет приветствие и краткий список доступных команд.
@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    event_payload = {
            "event_type": "command",
            "telegram_user_id": message.from_user.id,
            "chat_id": message.chat.id,
            "chat_type": message.chat.type,
            "command": "/start",
            "callback_type": None,
            "query":None,
            "cocktail_id":None,
            "cocktail_name":None,
            "status":"ok",
            "duration_ms":None,
            "error_type":None,
            "error_message":None,
            "metadata":None
        }
    await asyncio.to_thread(log_bot_event, **event_payload)
    await message.answer(f"""
        🍸 Cocktail Recipe Bot

Browse cocktail recipes from the database.

Available commands:
/cocktail <name> — show cocktail by exact name
/list — browse cocktails
/search <query> — search by cocktail name or ingredient
/help — show all commands

Examples:
/cocktail Abbey
/search gin
/search martini""")
