import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import list_cocktails
from utils.keyboards import get_cocktail_list_keyboard, back_to_list_keyboard
from services.cocktail_services import get_full_cocktail_by_id
from utils.cocktail_formatter import format_cocktail_text
from utils.cocktail_sender import send_cocktail_card


list_router = Router()

def build_cocktail_list_text(cocktails, page: int) -> str:
    return (
        f"🍸 Cocktails — Page {page}\n\n"
        f"Choose a cocktail:"
    )

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
    
    cocktails = list_cocktails(page)
    
    if not cocktails:
        return await message.answer("No more cocktails")

    text = build_cocktail_list_text(cocktails, page)
    
    await message.answer(
        text,
        reply_markup=get_cocktail_list_keyboard(cocktails, page),
    )

@list_router.callback_query(lambda callback: callback.data and callback.data.startswith("list:"))
async def list_callback_handler(callback: types.CallbackQuery):
    page = int(callback.data.split(":")[1])

    cocktails = list_cocktails(page)

    if not cocktails:
        await callback.answer("No more cocktails")
        return
    
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
    
    if not cocktail:
        await callback.answer("Cocktail not found")
        return
    
    text = format_cocktail_text(cocktail)

    await callback.message.delete()

    await send_cocktail_card(
        message=callback.message,
        cocktail=cocktail,
        text=text,
        reply_markup=back_to_list_keyboard(page),
    )
        
    await callback.answer()

@list_router.callback_query(lambda callback: callback.data == "noop")
async def noop_callback_handler(callback: types.CallbackQuery):
    await callback.answer("Already here")