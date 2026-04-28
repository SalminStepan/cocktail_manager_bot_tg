from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import get_full_cocktail_by_name

get_cocktail_router = Router()

@get_cocktail_router.message(Command("cocktail"))
async def cocktail_handler(message:types.Message):
    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /cocktail <name>")
        return
    else:
        name = " ".join(parse_msg[1:])
        cocktail = get_full_cocktail_by_name(name)
        if not cocktail:
            await message.answer("Cocktail not found")
            return
        lines = [f"🍸 {cocktail.name}",""]
        lines.append(f"Glass: {cocktail.glass}")
        lines.append(f"Method: {cocktail.method}")
        lines.append(f"Garnish: {cocktail.garnish}")
        lines.append("")
        lines.append(f"Ingredients:")
        for ingredient in cocktail.ingredients:
            line = f"- {ingredient.name} — {ingredient.amount} {ingredient.unit}"
            if ingredient.comment:
                line += (f"({ingredient.comment})")

            lines.append(line)
        text = "\n".join(lines)
        await message.answer(text)
