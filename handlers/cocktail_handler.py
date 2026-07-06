from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import get_full_cocktail_by_name
from utils.cocktail_formatter import format_cocktail_text

get_cocktail_router = Router()

@get_cocktail_router.message(Command("cocktail"))
async def cocktail_handler(message:types.Message):
    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /cocktail <name>")
        return
    
    name = " ".join(parse_msg[1:])
    cocktail = get_full_cocktail_by_name(name)

    if not cocktail:
        await message.answer("Cocktail not found")
        return

    text = format_cocktail_text(cocktail)

    if cocktail.image_url:
        await message.answer_photo(photo=cocktail.image_url, caption=text)
    else:
        await message.answer(text)