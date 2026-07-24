# Этот файл является точкой входа Telegram-бота.
# Здесь создаются Bot и Dispatcher, подключаются роутеры и настраивается меню команд перед запуском polling.

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import (
    BOT_TOKEN,
    COCKTAIL_API_BASE_URL,
    COCKTAIL_API_TIMEOUT,
)
from handlers.start_handler import start_router
from handlers.list_handler import list_router
from handlers.cocktail_handler import get_cocktail_router
from handlers.search_handler import search_router
from handlers.help_handler import help_router
# from handlers.add_handler import add_cocktail_router
# from handlers.delete_handler import delete_router
# from handlers.edit_handler import edit_router
# from handlers.edit_ingredient_handler import edit_ingredients_router
from clients.cocktail_api_client import CocktailApiClient


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

# Регистрирует видимые команды бота в Telegram-меню.
async def set_commands(bot: Bot):
        commands = [
            BotCommand(command="start", description="Start bot"),
            BotCommand(command="help", description="Show help"),
            BotCommand(command="list", description="List cocktails"),
            BotCommand(command="cocktail", description="Show recipe: /cocktail Negroni"),
            BotCommand(command="search", description="Search cocktails"),
            # BotCommand(command="add", description="Add cocktail (admin)"),
            # BotCommand(command="edit", description="Edit cocktail (admin)"),
            # BotCommand(command="edit_ingredients", description="Edit ingredients (admin)"),
            # BotCommand(command="delete", description="Delete cocktail (admin)"),
        ]

        await bot.set_my_commands(commands)
logger.info("Bot commands menu configured")

# Создает бота, подключает роутеры и запускает polling.
async def main():
    logger.info("Starting Cocktail Manager Bot")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    api_client = CocktailApiClient(
         base_url=COCKTAIL_API_BASE_URL,
         timeout=COCKTAIL_API_TIMEOUT,
    )
    
    dp.include_router(start_router)
    dp.include_router(list_router)
    dp.include_router(get_cocktail_router)
    dp.include_router(search_router)
    dp.include_router(help_router)
    # dp.include_router(add_cocktail_router)
    # dp.include_router(delete_router)
    # dp.include_router(edit_router)
    # dp.include_router(edit_ingredients_router)

    try:
        await set_commands(bot)
        await dp.start_polling(
            bot,
            api_client=api_client,
        )
    finally:
        await api_client.close()
        await bot.session.close()
        logger.info("Cocktail Manager Bot stopped")

if __name__ == "__main__":
    asyncio.run(main())
