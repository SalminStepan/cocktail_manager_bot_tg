# Этот файл содержит обработчик команды /help.
# Он вынесен отдельно, чтобы справка по командам не смешивалась с логикой поиска и карточек коктейлей.

import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command
from services.analytics_service import log_bot_event


help_router = Router()
# Отправляет справку по read-only командам бота.
@help_router.message(Command("help"))
async def start_handler(message: types.Message):
    event_payload = {
            "event_type": "command",
            "telegram_user_id": message.from_user.id,
            "chat_id": message.chat.id,
            "chat_type": message.chat.type,
            "command": "/help",
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
    await message.answer("""
        🍸 Commands:

/cocktail <name>
Show a cocktail recipe by exact name.
Example: /cocktail Abbey

/list
Browse cocktails page by page.

/search <query>
Search cocktails by name or ingredient.
Examples:
/search gin
/search martini
/search absinthe

Note:
The bot is currently read-only. Add/edit/delete commands are disabled after migration to the new ETL database.""")
