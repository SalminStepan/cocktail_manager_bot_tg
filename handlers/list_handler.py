from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import list_cocktails
from utils.keyboards import get_cocktail_list_keyboard

list_router = Router()

def build_cocktail_list_text(cocktails, page: int) -> str:
    page_size = 20
    start_index = (page - 1) * page_size

    lines = [f"🍸 Cocktails (Page {page})", ""]
    
    for i, cocktail in enumerate(cocktails):
        number = start_index + i + 1
        lines.append(f"{number}. {cocktail['name']}")

    return "\n".join(lines)

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

    await callback.message.edit_text(
        text,
        reply_markup=get_cocktail_list_keyboard(cocktails, page),
    )
    await callback.answer()