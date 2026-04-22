from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import delete_cocktail_by_name
from config import ADMIN_IDS

delete_router = Router()

@delete_router.message(Command("delete"))
async def delete_cocktail_handler(message:types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Access denied")
        return
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("Usage: /delete <cocktail name>")
        return
    name = " ".join(parts[1:])
    cocktail_id = delete_cocktail_by_name(name)
    if cocktail_id is None:
        await message.answer("Cocktail not found")
        return
    await message.answer(f"Cocktail deleted (id: {cocktail_id})")