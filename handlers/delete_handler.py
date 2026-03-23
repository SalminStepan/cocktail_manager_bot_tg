from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import delete_cocktail_by_name

delete_router = Router()

@delete_router.message(Command("delete"))
async def delete_cocktail_handler(message:types.Message):
    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /delete <query>")
        return
    name = " ".join(parse_msg[1:])
    cocktail_id = delete_cocktail_by_name(name)
    if cocktail_id is None:
        await message.answer("Cocktail not found")
        return
    await message.answer(f"Cocktail deleted (id: {cocktail_id})")