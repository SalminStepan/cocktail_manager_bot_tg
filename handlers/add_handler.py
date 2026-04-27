import logging
from aiogram import Router, types
from aiogram.filters.command import Command
from schemas.cocktail import CocktailCreate
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.cocktail_services import create_cocktail_with_ingredients
from config import ADMIN_IDS

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
        logger.warning(f"Unauthorized /add attempt by user {user_id}")
        await message.answer("Access denied")
        return
    
    logger.info(f"User {user_id} started /add")

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
        "Allowed units: ml, dash, pcs, g\n"
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
    
    logger.info("User %s cerated cocktail '%s' (id=%s)",
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

    ALLOWED_UNITS = {"ml", "dash", "pcs", "g", "cube", "bspn"}
    parts = message.text.split()

    idx = None
    for i, part in enumerate(parts):
        if part.isdigit():
            idx = i
            break

    if idx is None:
        return await message.answer(
            "Invalid format. Example: Gin 30 ml or Tonic 80 ml on_top"
        )

    if idx + 1 >= len(parts):
        return await message.answer("Need unit after amount")

    name = " ".join(parts[:idx]).strip()
    if not name:
        return await message.answer("Ingredient name is required")

    amount = int(parts[idx])
    if amount <= 0:
        return await message.answer("Amount must be greater than 0")

    unit = parts[idx + 1].strip().lower()
    if unit not in ALLOWED_UNITS:
        return await message.answer("Invalid unit. Allowed units: ml, dash, pcs, g")

    comment_parts = parts[idx + 2:]
    comment = " ".join(comment_parts).strip() if comment_parts else None

    data = await state.get_data()
    ingredients = data.get("ingredients", [])
    ingredients.append(
        {
            "name": name,
            "amount": amount,
            "unit": unit,
            "comment": comment,
        }
    )
    await state.update_data(ingredients=ingredients)

    if comment:
        await message.answer(
            f"Ingredient added: {name} {amount} {unit} ({comment})\n"
            f"Send next ingredient or /done\n"
            f"Send /cancel to cancel operation"
        )
    else:
        await message.answer(
            f"Ingredient added: {name} {amount} {unit}\n"
            f"Send next ingredient or /done\n"
            f"Send /cancel to cancel operation"
        )