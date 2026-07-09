# Этот файл обрабатывает команду /cocktail для просмотра рецепта по точному названию.
# Он связывает Telegram-команду с сервисным слоем, форматтером карточки и отправкой текста или фото.
import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command

from services.cocktail_services import get_full_cocktail_by_name
from utils.cocktail_formatter import format_cocktail_text
from utils.cocktail_sender import send_cocktail_card
from services.analytics_service import log_bot_event


get_cocktail_router = Router()

# Обрабатывает /cocktail и отправляет найденную карточку рецепта.
@get_cocktail_router.message(Command("cocktail"))
async def cocktail_handler(message:types.Message):
    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /cocktail <name>")
        return
    
    name = " ".join(parse_msg[1:])
    cocktail = await asyncio.to_thread(get_full_cocktail_by_name, name)

    if cocktail:
        event_payload = {
            "event_type": "cocktail_view",
            "telegram_user_id": message.from_user.id,
            "chat_id": message.chat.id,
            "chat_type": message.chat.type,
            "command":"/cocktail",
            "callback_type": None,
            "query": name,
            "cocktail_id": cocktail.id,
            "cocktail_name": cocktail.name,
            "status": "ok",
            "duration_ms": None,
            "error_type": None,
            "error_message": None,
            "metadata": {"source": "command"}
        }
    else:
        event_payload = {
            "event_type": "cocktail_view",
            "telegram_user_id": message.from_user.id,
            "chat_id": message.chat.id,
            "chat_type": message.chat.type,
            "command": "/cocktail",
            "callback_type": None,
            "query": name,
            "cocktail_id": None,
            "cocktail_name": None,
            "status": "not_found",
            "duration_ms": None,
            "error_type": None,
            "error_message": None,
            "metadata": {"source": "command"}
        }

    if not cocktail:
        await asyncio.to_thread(
            log_bot_event,** event_payload)
        await message.answer("Cocktail not found")
        return

    await asyncio.to_thread(
        log_bot_event,**event_payload)

    text = format_cocktail_text(cocktail)

    await send_cocktail_card(
        message=message,
        cocktail=cocktail,
        text=text,
    )