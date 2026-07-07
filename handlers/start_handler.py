from aiogram import Router, types
from aiogram.filters.command import Command


#router
start_router = Router()
#start
@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"""
        🍸 Cocktail Recipe Bot

Browse cocktail recipes from the database.

Available commands:
/cocktail <name> — show cocktail by exact name
/list — browse cocktails
/search <query> — search by cocktail name or ingredient
/help — show all commands

Examples:
/cocktail Abbey
/search gin
/search martini""")