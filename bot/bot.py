from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
from handlers.start import router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())