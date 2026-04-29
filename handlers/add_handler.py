import logging
from aiogram import Router, types
from aiogram.filters.command import Command
from schemas.cocktail import CocktailCreate
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.cocktail_services import create_cocktail_with_ingredients
from config import ADMIN_IDS
from utils.ingredient_parser import parse_ingredient_input

logger = logging.getLogger(__name__)

add_cocktail_router = Router()

class AddCocktail(StatesGroup):
    name = State()
    glass = State()
    garnish = State()
    method = State()
    ingredients = State()

# add
@add_cocktail_router.message(Command("add"))
async def add_cocktail_handler(message:types.Message, state:FSMContext):
    user_id = message.from_user.id

    if user_id not in ADMIN_IDS:
        logger.warning("Unauthorized /add attempt by user %s", user_id)
        await message.answer("Access denied")
        return
    
    logger.info("User %s started /add", user_id)

    await state.clear()
    await message.answer("Enter cocktail name")
    await state.set_state(AddCocktail.name)

# cancel
@add_cocktail_router.message(Command("cancel"))
async def cancel_handler(message:types.Message, state:FSMContext):
    user_id = message.from_user.id
    state_now = await state.get_state()

    if state_now is None:
        await message.answer("Nothing to cancel")
    else:
        logger.info("User %s cancelled state %s", user_id, state_now)
        await state.clear()
        await message.answer("Operation cancelled")

# name
@add_cocktail_router.message(AddCocktail.name)
async def name_handler(message:types.Message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Enter glass")
    await state.set_state(AddCocktail.glass)

# glass
@add_cocktail_router.message(AddCocktail.glass)
async def glass_handler(message:types.Message, state:FSMContext):
    await state.update_data(glass=message.text)
    await message.answer("Enter garnish")
    await state.set_state(AddCocktail.garnish)

# garnish
@add_cocktail_router.message(AddCocktail.garnish)
async def garnish_handler(message:types.Message, state:FSMContext):
    await state.update_data(garnish=message.text)
    await message.answer("Enter method")
    await state.set_state(AddCocktail.method)

# method
@add_cocktail_router.message(AddCocktail.method)
async def method_handler(message: types.Message, state: FSMContext):
    await state.update_data(method=message.text)
    await state.update_data(ingredients = [])
    await message.answer(
        "Enter ingredient in format: name amount unit [comment]\n"
        "Example: Gin 30 ml\n"
        "Example: Tonic 80 ml on_top\n"
        "Allowed units: ml, dash, pcs, g, cube, bspn\n"
        "Send /done when finished\n"
        "Send /cancel to cancel operation"
    )
    await state.set_state(AddCocktail.ingredients)
# done
@add_cocktail_router.message(Command("done"), AddCocktail.ingredients)
async def done_handler(message:types.Message, state:FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    ingredients_data = data.get("ingredients", [])
    
    if not ingredients_data:
        return await message.answer("Cocktail cannot be created without ingredients")
    
    try:
        cocktail = CocktailCreate(**data)
        cocktail_id = create_cocktail_with_ingredients(cocktail)
    except Exception:
        logger.error(
            "Cocktail creation failed for user %s (data=%s)",
            user_id,
            data,
            exc_info=True
        )
        await state.clear()
        return await message.answer("Cocktail creation failed")
    
    logger.info("User %s created cocktail '%s' (id=%s)",
        user_id, 
        cocktail.name, 
        cocktail_id
    )
    await message.answer(f"Cocktail created with id: {cocktail_id}")
    await state.clear()

# ingredients
@add_cocktail_router.message(AddCocktail.ingredients)
async def ingredient_handler(message: types.Message, state: FSMContext):
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