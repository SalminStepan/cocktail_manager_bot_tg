# Этот файл содержит обработчик команды /help.
# Он вынесен отдельно, чтобы справка по командам не смешивалась с логикой поиска и карточек коктейлей.

from aiogram import Router, types
from aiogram.filters.command import Command


help_router = Router()
# Отправляет справку по read-only командам бота.
@help_router.message(Command("help"))
async def start_handler(message: types.Message):
    await message.answer("""
        🍸 Commands:

/cocktail <name>
Show a cocktail recipe by exact name.
Example: /cocktail Abbey

/list
Browse cocktails page by page.

/search <query>
Search cocktails by name or ingredient.
Examples:
/search gin
/search martini
/search absinthe

Note:
The bot is currently read-only. Add/edit/delete commands are disabled after migration to the new ETL database.""")
