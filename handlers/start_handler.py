from aiogram import Router, types
from aiogram.filters.command import Command


#router
start_router = Router()
#start
@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"""
        🍸 Cocktail Manager Bot
            
        Manage your cocktail recipes:
        - add new cocktails
        - search and view recipes
        - delete entries

        Type /help to see all commands.""")