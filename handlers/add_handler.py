from aiogram import Router, types
from aiogram.filters.command import Command
from schemas.cocktail import CocktailCreate
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.cocktail_services import create_cocktail_with_ingredients
from config import ADMIN_IDS

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
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Access denied")
        return
    await state.clear()
    await message.answer("Enter cocktail name")
    await state.set_state(AddCocktail.name)
# cancel
@add_cocktail_router.message(Command("cancel"))
async def cancel_handler(message:types.Message, state:FSMContext):
    state_now = await state.get_state()
    if state_now is None:
        await message.answer("Nothing to cancel")
    else:
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
    await message.answer("""
Enter ingredient in format: name amount_ml
Example: Gin 30
Send /done when finished
Send /cancel to cancel operation""")
    await state.set_state(AddCocktail.ingredients)
# done
@add_cocktail_router.message(Command("done"), AddCocktail.ingredients)
async def done_handler(message:types.Message, state:FSMContext):
    data = await state.get_data()
    ingredients_data = data.get("ingredients", [])
    if not ingredients_data:
        return await message.answer("Cocktail cannot be created without ingredients")
    try:
        cocktail = CocktailCreate(**data)
        cocktail_id = create_cocktail_with_ingredients(cocktail)
    except Exception:
        await state.clear()
        return await message.answer("Cocktail creation failed")
    await message.answer(f"Cocktail created with id: {cocktail_id}")
    await state.clear()
# ingredients
@add_cocktail_router.message(AddCocktail.ingredients)
async def ingredient_handler(message:types.Message, state:FSMContext):
    if message.text.startswith("/"):
        return
    parts = message.text.split()
    if len(parts) < 2:
        return await message.answer("Invalid format. Example: Gin 30")
    name =" ".join(parts[:-1])
    try:
        amount_ml = int(parts[-1])
        if amount_ml <= 0:
            return await message.answer("Amount must be greater than 0")
    except ValueError:
        return await message.answer("Amount must be an integer")
    data = await state.get_data()
    ingredients = data.get("ingredients", [])
    ingredients.append({"name":name, "amount_ml": amount_ml})
    await state.update_data(ingredients=ingredients)
    await message.answer(f"""
Ingredient added: {name} {amount_ml} ml
Send next ingredient or /done
Send /cancel to cancel operation""")
