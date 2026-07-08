# Этот файл отвечает за поиск коктейлей по названию или ингредиенту в Telegram.
# Здесь собрана логика команды /search, callback-пагинации, открытия карточки из результатов и записи поисковой аналитики.

import asyncio
from aiogram import Router, types
from aiogram.filters.command import Command

from services.cocktail_services import search_by_query
from utils.keyboards import search_results_keyboard, back_to_search_keyboard
from services.cocktail_services import get_full_cocktail_by_id
from utils.cocktail_formatter import format_cocktail_text
from utils.cocktail_sender import send_cocktail_card
from services.analytics_service import log_bot_event


search_router = Router()

# Собирает заголовок страницы результатов поиска.
def build_cocktail_search_text(page: int, query: str) -> str:
    return (
        f"🍸 Search results for {query}\n"
        f"Page {page}\n"
        f"Choose a cocktail:\n\n"
    )


# Обрабатывает /search, ищет коктейли и логирует результат.
@search_router.message(Command("search"))
async def search_handler(message:types.Message):
    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /search <query>")
        return

    query = " ".join(parse_msg[1:])
    query = " ".join(query.strip().replace(":", " ").split())[:20]
    page = 1

    cocktails = await asyncio.to_thread(search_by_query, query, page)

    if cocktails:
        event_type="search"
        telegram_user_id=message.from_user.id
        chat_id=message.chat.id
        chat_type=message.chat.type
        command="/search"
        callback_type=None
        query=query
        cocktail_id=None
        cocktail_name=None
        status="ok"
        duration_ms=None
        error_type=None
        error_message=None
        metadata={"results_count": len(cocktails), "page":page}
    else:
        event_type="search"
        telegram_user_id=message.from_user.id
        chat_id=message.chat.id
        chat_type=message.chat.type
        command="/search"
        callback_type=None
        query=query
        cocktail_id=None
        cocktail_name=None
        status="not_found"
        duration_ms=None
        error_type=None
        error_message=None
        metadata={"results_count": 0, "page": page}

    if not cocktails:
        await asyncio.to_thread(
            log_bot_event,
            event_type=event_type,
            telegram_user_id=telegram_user_id,
            chat_id=chat_id,
            chat_type=chat_type,
            command=command,
            callback_type=callback_type,
            query=query,
            cocktail_id=cocktail_id,
            cocktail_name=cocktail_name,
            status=status,
            duration_ms=duration_ms,
            error_type=error_type,
            error_message=error_message,
            metadata=metadata
        )
        return await message.answer("Nothing found")

    await asyncio.to_thread(
        log_bot_event,
        event_type=event_type,
        telegram_user_id=telegram_user_id,
        chat_id=chat_id,
        chat_type=chat_type,
        command=command,
        callback_type=callback_type,
        query=query,
        cocktail_id=cocktail_id,
        cocktail_name=cocktail_name,
        status=status,
        duration_ms=duration_ms,
        error_type=error_type,
        error_message=error_message,
        metadata=metadata
    )

    text = build_cocktail_search_text(page, query)

    await message.answer(
        text,
        reply_markup=search_results_keyboard(cocktails, page, query),
    )


# Переключает страницы результатов поиска по inline-кнопкам.
@search_router.callback_query(lambda callback: callback.data and callback.data.startswith("s_p:"))
async def search_callback_handler(callback: types.CallbackQuery):
    page = int(callback.data.split(":")[1])
    query = str(callback.data.split(":")[-1])

    cocktails = await asyncio.to_thread(search_by_query, query, page)

    if not cocktails:
        await callback.answer("No more cocktails")
        return

    text = build_cocktail_search_text(page, query)

    if callback.message.text:
        await callback.message.edit_text(
            text,
            reply_markup=search_results_keyboard(cocktails, page, query),
        )
    else:
        await callback.message.delete()
        await callback.message.answer(
            text,
            reply_markup=search_results_keyboard(cocktails, page, query),
        )
    await callback.answer()

# Открывает карточку коктейля из результатов поиска.
@search_router.callback_query(lambda callback:callback.data and callback.data.startswith('s_c:'))
async def search_cocktail_from_key_handler(callback: types.CallbackQuery):
    try:
        parts = callback.data.split(':')
        cocktail_id = int(parts[1])
        page = int(parts[2])
        query = str(callback.data.split(":")[-1])
    except (IndexError, ValueError):
        await callback.answer("Invalid callback data")
        return

    cocktail = await asyncio.to_thread(get_full_cocktail_by_id, cocktail_id)

    if not cocktail:
        await callback.answer("Cocktail not found")
        return

    text = format_cocktail_text(cocktail)

    await callback.message.delete()

    await send_cocktail_card(
        message=callback.message,
        cocktail=cocktail,
        text=text,
        reply_markup=back_to_search_keyboard(page, query),
    )
    await callback.answer()

# Отвечает на неактивную кнопку текущей страницы.
@search_router.callback_query(lambda callback: callback.data == "noop")
async def noop_callback_handler(callback: types.CallbackQuery):
    await callback.answer("Already here")
