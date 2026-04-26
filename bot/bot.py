from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
from handlers.start_handler import start_router
from tests.add_test_handler import add_router
from handlers.list_handler import list_router
from handlers.cocktail_handler import get_cocktail_router
from handlers.search_handler import search_router
from handlers.add_handler import add_cocktail_router
from handlers.delete_handler import delete_router
from handlers.help_handler import help_router
from handlers.edit_handler import edit_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(add_router)
    dp.include_router(list_router)
    dp.include_router(get_cocktail_router)
    dp.include_router(search_router)
    dp.include_router(add_cocktail_router)
    dp.include_router(delete_router)
    dp.include_router(help_router)
    dp.include_router(edit_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())