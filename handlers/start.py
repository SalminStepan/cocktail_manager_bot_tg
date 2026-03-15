from aiogram import Router, types
from aiogram.filters.command import Command


#router
router = Router()
#start
@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Cocktail Manager Bot is running.")

