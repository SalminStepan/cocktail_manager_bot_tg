from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import list_cocktails

list_router = Router()

@list_router.message(Command("list"))
async def list_handler(message:types.Message):
    cocktails = list_cocktails() 
    if not cocktails:
        await message.answer("Cocktail list empty")
    else:
        lines = ["🍸 Cocktails",""]
        for i, cocktail in enumerate(cocktails, start=1):
            lines.append(f'{i}. {cocktail["name"]}')
        text = "\n".join(lines)
        await message.answer(text)