from aiogram import Router, types
from aiogram.filters.command import Command


#router
help_router = Router()
#help
@help_router.message(Command("help"))
async def start_handler(message: types.Message):
    await message.answer("""
        🍸 Commands:

        /add — create a new cocktail (step-by-step)
        /list — show cocktail list
        /cocktail <name> — show full recipe
        /search <query> — search cocktails
        /delete <name> — delete cocktail

        Example:
        /cocktail Negroni
        /search gin""")