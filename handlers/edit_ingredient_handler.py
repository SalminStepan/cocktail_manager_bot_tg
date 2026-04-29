import logging
from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.cocktail_services import replace_cocktail_ingredients_by_name, get_full_cocktail_by_name
from config import ADMIN_IDS
from utils.ingredient_parser import parse_ingredient_input
import asyncio

logger = logging.getLogger(__name__)

edit_ingredients_router = Router()

class EditIngredients(StatesGroup):
    ingredients = State()

@edit_ingredients_router.message(Command("edit_ingredients"))
async def edit_ingredients(message:types.Message, state:FSMContext):
    user_id = message.from_user.id
    
    if user_id not in ADMIN_IDS:
        logger.warning("Unauthorized /edit_ingredients attempt by user %s", user_id)
        await message.answer("Access denied")
        return

    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /edit_ingredients <name>")
        return
    else:
        name = " ".join(parse_msg[1:])
        logger.info("User %s started /edit_ingredients '%s'", user_id, name)
        cocktail = await asyncio.to_thread(get_full_cocktail_by_name, name)
        if not cocktail:
            await message.answer("Cocktail not found")
            logger.warning(
                "User %s tried to edit ingredients for non-existing cocktail '%s'",
                user_id,
                name,
            )
            return
        lines = [f"🍸 {cocktail.name}", "", "Ingredients:"]
        for ingredient in cocktail.ingredients:
            line = f"- {ingredient.name} — {ingredient.amount} {ingredient.unit}"
            if ingredient.comment:
                line += f" ({ingredient.comment})"

            lines.append(line)
        text = "\n".join(lines)
        await state.clear()
        await state.update_data(name=name, ingredients = [])
        await message.answer(text)
        await message.answer("""Enter ingredients (one per line): name amount unit [comment]
Send /done when finished or /cancel""")
        await state.set_state(EditIngredients.ingredients)

@edit_ingredients_router.message(Command("cancel"), EditIngredients.ingredients)
async def edit_cancel_handler(message:types.Message, state:FSMContext):
    user_id = message.from_user.id
    state_now = await state.get_state()

    if state_now is None:
        await message.answer("Nothing to cancel")
    else:
        logger.info("User %s cancelled state %s", user_id, state_now)
        await state.clear()
        await message.answer("Operation cancelled")

@edit_ingredients_router.message(EditIngredients.ingredients)
async def ingredients_handler(message:types.Message, state:FSMContext):
    if not message.text or message.text.startswith("/"):
        return
    try:
        parsed = parse_ingredient_input(message.text)
    except ValueError as e:
        return await message.answer(str(e))
    data = await state.get_data()
    ingredients = data.get("ingredients", [])
    ingredients.append(parsed)
    await state.update_data(ingredients=ingredients)
    logger.info(
        "User %s added ingredient: %s",
        message.from_user.id,
        parsed,
    )
    line = f"{parsed['name']} {parsed['amount']} {parsed['unit']}"

    if parsed["comment"]:
        line += f" ({parsed['comment']})"

    await message.answer(
        f"Ingredient added: {line}\n"
        f"Send next ingredient or /done\n"
        f"Send /cancel to cancel operation"
    )

@edit_ingredients_router.message(Command("done"), EditIngredients.ingredients)
async def done_handler(message:types.Message, state:FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    ingredients_data = data.get("ingredients", [])
    name = data.get("name")
    if not ingredients_data:
        logger.warning(
            "User %s tried to replace ingredients with empty list for '%s'",
            user_id,
            name,
        )
        return await message.answer("Need ingredients")

    try:
        cocktail_id = await asyncio.to_thread(
            replace_cocktail_ingredients_by_name,
            name,
            ingredients_data,
        )
    except Exception:
        logger.error(
            "Cocktail replace failed for user %s (data=%s)",
            user_id,
            data,
            exc_info=True
        )
        await message.answer("Update failed")
        await state.clear()
        return

    if cocktail_id is None:
        logger.warning(
            "User %s tried to replace ingredients for non-existing cocktail '%s'",
            user_id,
            name,
        )
        await state.clear()
        return await message.answer("Cocktail not found")

    await message.answer("Ingredients updated")
    await state.clear()
    logger.info("User %s replaced ingredients in cocktail '%s' (id=%s)",
        user_id, 
        name, 
        cocktail_id
    )