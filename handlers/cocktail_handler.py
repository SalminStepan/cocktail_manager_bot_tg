from aiogram import Router, types
from aiogram.filters.command import Command

from services.cocktail_services import get_full_cocktail_by_name
from utils.cocktail_formatter import format_cocktail_text
from utils.cocktail_sender import send_cocktail_card


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

    await send_cocktail_card(
        message=message,
        cocktail=cocktail,
        text=text,
    )