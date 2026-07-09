# Этот файл отвечает за команду /list и навигацию по списку коктейлей.
# Он держит Telegram callback-логику отдельно от сервисов, чтобы пагинация и кнопки не попадали в слой базы.

import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import list_cocktails
from utils.keyboards import get_cocktail_list_keyboard, back_to_list_keyboard
from services.cocktail_services import get_full_cocktail_by_id
from utils.cocktail_formatter import format_cocktail_text
from utils.cocktail_sender import send_cocktail_card
from services.analytics_service import log_bot_event


list_router = Router()

# Собирает заголовок страницы списка коктейлей.
def build_cocktail_list_text(cocktails, page: int) -> str:
    return (
        f"🍸 Cocktails — Page {page}\n\n"
        f"Choose a cocktail:"
    )

# Обрабатывает /list и показывает страницу коктейлей с кнопками.
@list_router.message(Command("list"))
async def list_handler(message:types.Message):
    parse_msg = message.text.split()
    
    if len(parse_msg) == 1:
        page = 1
    elif len(parse_msg) == 2:
        page = parse_msg[1]
        try:
            page = int(page)
            if page < 1:
                page = 1
        except ValueError:
            await message.answer("Page must be an integer")
            return

    else:
        await message.answer("Usage: /list <page>")
        return
    
    cocktails = await asyncio.to_thread(list_cocktails, page)

    if cocktails:
        event_payload = {
            "event_type": "list",
            "telegram_user_id": message.from_user.id,
            "chat_id": message.chat.id,
            "chat_type": message.chat.type,
            "command": "/list",
            "callback_type": None,
            "query": None,
            "cocktail_id": None,
            "cocktail_name": None,
            "status":"ok",
            "duration_ms": None,
            "error_type": None,
            "error_message": None,
            "metadata": {"results_count": len(cocktails), "page":page},
        }
    else:
        event_payload = {
            "event_type": "list",
            "telegram_user_id": message.from_user.id,
            "chat_id": message.chat.id,
            "chat_type": message.chat.type,
            "command": "/list",
            "callback_type": None,
            "query":None,
            "cocktail_id":None,
            "cocktail_name":None,
            "status":"empty_page",
            "duration_ms":None,
            "error_type":None,
            "error_message":None,
            "metadata":{"results_count": 0, "page": page}
        }
    
    if not cocktails:
        await asyncio.to_thread(log_bot_event, **event_payload)
        return await message.answer("No more cocktails")

    await asyncio.to_thread(log_bot_event, **event_payload)

    text = build_cocktail_list_text(cocktails, page)
    
    await message.answer(
        text,
        reply_markup=get_cocktail_list_keyboard(cocktails, page),
    )

# Переключает страницы списка по inline-кнопкам.
@list_router.callback_query(lambda callback: callback.data and callback.data.startswith("list:"))
async def list_callback_handler(callback: types.CallbackQuery):
    page = int(callback.data.split(":")[1])

    cocktails = await asyncio.to_thread(list_cocktails, page)

    if cocktails:
        event_payload = {
            "event_type": "pagination",
            "telegram_user_id": callback.from_user.id,
            "chat_id": callback.message.chat.id,
            "chat_type": callback.message.chat.type,
            "command": None,
            "callback_type": "list_page",
            "query": None,
            "cocktail_id": None,
            "cocktail_name": None,
            "status":"ok",
            "duration_ms": None,
            "error_type": None,
            "error_message": None,
            "metadata": {"results_count": len(cocktails), "page":page},
        }
    else:
        event_payload = {
            "event_type": "pagination",
            "telegram_user_id": callback.from_user.id,
            "chat_id": callback.message.chat.id,
            "chat_type": callback.message.chat.type,
            "command": None,
            "callback_type": "list_page",
            "query": None,
            "cocktail_id": None,
            "cocktail_name": None,
            "status": "empty_page",
            "duration_ms": None,
            "error_type": None,
            "error_message": None,
            "metadata":{"results_count": 0, "page": page}
        }

    if not cocktails:
        await asyncio.to_thread(log_bot_event, **event_payload)
        await callback.answer("No more cocktails")
        return
    
    await asyncio.to_thread(log_bot_event, **event_payload)

    text = build_cocktail_list_text(cocktails, page)

    if callback.message.text:
        await callback.message.edit_text(
            text,
            reply_markup=get_cocktail_list_keyboard(cocktails, page),
        )
    else:
        await callback.message.delete()
        await callback.message.answer(
            text,
            reply_markup=get_cocktail_list_keyboard(cocktails, page),
        )
    await callback.answer()

# Открывает карточку коктейля из кнопки списка.
@list_router.callback_query(lambda callback:callback.data and callback.data.startswith('cocktail:'))
async def cocktail_from_key_handler(callback: types.CallbackQuery):
    try:
        parts = callback.data.split(':')
        cocktail_id = int(parts[1])
        page = int(parts[2])
    except (IndexError, ValueError):
        await callback.answer("Invalid callback data")
        return
    
    cocktail = await asyncio.to_thread(get_full_cocktail_by_id, cocktail_id)

    if cocktail:
        event_payload = {
            "event_type": "cocktail_view",
            "telegram_user_id": callback.from_user.id,
            "chat_id": callback.message.chat.id,
            "chat_type": callback.message.chat.type,
            "command": None,
            "callback_type": "list_detail",
            "query": None,
            "cocktail_id": cocktail.id,
            "cocktail_name": cocktail.name,
            "status":"ok",
            "duration_ms": None,
            "error_type": None,
            "error_message": None,
            "metadata": {"page":page},
        }
    else:
        event_payload = {
            "event_type": "cocktail_view",
            "telegram_user_id": callback.from_user.id,
            "chat_id": callback.message.chat.id,
            "chat_type": callback.message.chat.type,
            "command": None,
            "callback_type": "list_detail",
            "query": None,
            "cocktail_id": cocktail_id,
            "cocktail_name": None,
            "status": "not_found",
            "duration_ms": None,
            "error_type": None,
            "error_message": None,
            "metadata": {"page":page}
        }    

    if not cocktail:
        await asyncio.to_thread(log_bot_event, **event_payload)
        await callback.answer("Cocktail not found")
        return

    await asyncio.to_thread(log_bot_event, **event_payload)

    text = format_cocktail_text(cocktail)

    await callback.message.delete()

    await send_cocktail_card(
        message=callback.message,
        cocktail=cocktail,
        text=text,
        reply_markup=back_to_list_keyboard(page),
    )
        
    await callback.answer()

# Отвечает на неактивную кнопку текущей страницы.
@list_router.callback_query(lambda callback: callback.data == "noop")
async def noop_callback_handler(callback: types.CallbackQuery):
    await callback.answer("Already here")
