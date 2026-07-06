import asyncio
from aiogram import Router, types
from aiogram.filters.command import Command

from services.cocktail_services import search_by_query
from utils.keyboards import search_results_keyboard, back_to_search_keyboard
from services.cocktail_services import get_full_cocktail_by_id
from utils.cocktail_formatter import format_cocktail_text

search_router = Router()

def build_cocktail_search_text(page: int, query: str) -> str:
    return (
        f"🍸 Search results for {query}\n"
        f"Page {page}\n"
        f"Choose a cocktail:\n\n"
    )


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
    
    if not cocktails:
        return await message.answer("Nothing found")
    
    text = build_cocktail_search_text(page, query)
    
    await message.answer(
        text,
        reply_markup=search_results_keyboard(cocktails, page, query),
    )


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

    if cocktail.image_url:
        await callback.message.answer_photo(photo=cocktail.image_url, caption=text, reply_markup=back_to_search_keyboard(page, query))
    else:
        await callback.message.answer(text, reply_markup=back_to_search_keyboard(page, query))
        
    await callback.answer()

@search_router.callback_query(lambda callback: callback.data == "noop")
async def noop_callback_handler(callback: types.CallbackQuery):
    await callback.answer("Already here")