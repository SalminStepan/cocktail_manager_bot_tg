from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.cocktail_services import update_cocktail_by_name, get_full_cocktail_by_name
from config import ADMIN_IDS
import asyncio

edit_router = Router()

#create fsm class
class EditCocktail(StatesGroup):
    select_field = State()
    new_value = State()

#edit <cocktail_name> cmd
@edit_router.message(Command("edit"))
async def edit_cocktail_handler(message:types.Message, state:FSMContext):
    await state.clear()    
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Access denied")
        return
    parse_msg = message.text.split()
    if len(parse_msg) < 2:
        await message.answer("Usage: /edit <cocktail name>")
        return
    name = " ".join(parse_msg[1:])
    cocktail = await asyncio.to_thread(get_full_cocktail_by_name, name)
    if not cocktail:
        await message.answer("Cocktail not found")
        return
    await state.update_data(name=name)

    await message.answer("""What do you want to edit?
glass / garnish / method""")
    await state.set_state(EditCocktail.select_field)
# exit cmd
@edit_router.message(Command("cancel"), EditCocktail)
async def edit_cancel_handler(message:types.Message, state:FSMContext):
    state_now = await state.get_state()
    if state_now is None:
        await message.answer("Nothing to cancel")
    else:
        await state.clear()
        await message.answer("Operation cancelled")
#select field cmd
@edit_router.message(EditCocktail.select_field)
async def select_field_handler(message:types.Message, state:FSMContext):
    fields = {"glass", "garnish", "method"}
    field = message.text.strip().lower()
    if field not in fields:
        await message.answer("Invalid field. Choose: glass / garnish / method")
        return
    await state.update_data(field=field)
    await message.answer("Enter new value")
    await state.set_state(EditCocktail.new_value)
#new value cmd
@edit_router.message(EditCocktail.new_value)
async def new_value_handler(message:types.Message, state:FSMContext):
    if not message.text or message.text.isspace() or message.text.startswith("/"):
        await message.answer("Send new value")
        return
    new_value = message.text.strip()
    data = await state.get_data()
    name = data["name"]
    field = data["field"]
    cocktail_id = await asyncio.to_thread(update_cocktail_by_name, name, field, new_value)
    if not cocktail_id:
        await message.answer("Update failed or cocktail not found")
        await state.clear()
        return
    await message.answer(f"{field.capitalize()} updated")
    await state.clear()