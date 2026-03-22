from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
from handlers.start import start_router
from handlers.add_test import add_router
from handlers.get_all import list_router
from handlers.get_cocktail_by_name import get_cocktail_router
from handlers.search import search_router
from handlers.add_hadler import add_cocktail_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(add_router)
    dp.include_router(list_router)
    dp.include_router(get_cocktail_router)
    dp.include_router(search_router)
    dp.include_router(add_cocktail_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())