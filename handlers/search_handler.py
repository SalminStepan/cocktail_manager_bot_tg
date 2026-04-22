from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import search_by_query

search_router = Router()

@search_router.message(Command("search"))
async def search_handler(message:types.Message):
    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /search <query>")
        return
    query = " ".join(parse_msg[1:])
    cocktails = search_by_query(query)
    if not cocktails:
        await message.answer("Nothing found")
        return
    lines =  [f"🍸 Search results",""]
    for i, cocktail in enumerate(cocktails, start=1):
        lines.append(f'{i}. {cocktail["name"]}')
    text = "\n".join(lines)
    await message.answer(text)