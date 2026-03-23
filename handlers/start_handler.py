from aiogram import Router, types
from aiogram.filters.command import Command


#router
start_router = Router()
#start
@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Cocktail Manager Bot is running.")

