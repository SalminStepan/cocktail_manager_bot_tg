from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.cocktail_services import update_cocktail_by_name, get_full_cocktail_by_name
from config import ADMIN_IDS
import asyncio
import logging

logger = logging.getLogger(__name__)
edit_router = Router()

#create fsm class
class EditCocktail(StatesGroup):
    select_field = State()
    new_value = State()

#edit <cocktail_name> cmd
@edit_router.message(Command("edit"))
async def edit_cocktail_handler(message:types.Message, state:FSMContext):
    user_id = message.from_user.id

    await state.clear()    
    
    if user_id not in ADMIN_IDS:
        logger.warning("Unauthorized /edit attempt by user %s", user_id)
        await message.answer("Access denied")
        return
    
    parse_msg = message.text.split()
    
    if len(parse_msg) < 2:
        await message.answer("Usage: /edit <cocktail name>")
        return
    
    name = " ".join(parse_msg[1:])
    logger.info("User %s requested edit for '%s'", user_id, name)

    cocktail = await asyncio.to_thread(get_full_cocktail_by_name, name)
    if not cocktail:
        logger.warning("User %s tried to edit non-existing cocktail '%s'", user_id, name)
        await message.answer("Cocktail not found")
        return
    await state.update_data(name=name)
    await message.answer("""What do you want to edit?
- glass
- garnish
- method""")
    await state.set_state(EditCocktail.select_field)

# cancel cmd
@edit_router.message(Command("cancel"), EditCocktail)
async def edit_cancel_handler(message:types.Message, state:FSMContext):
    state_now = await state.get_state()
    if state_now is None:
        await message.answer("Nothing to cancel")
    else:
        logger.info(
            "User %s cancelled edit flow from state %s",
            message.from_user.id,
            state_now,
        )
        await state.clear()
        await message.answer("Operation cancelled")

#select field cmd
@edit_router.message(EditCocktail.select_field)
async def select_field_handler(message:types.Message, state:FSMContext):
    fields = {"glass", "garnish", "method"}
    field = message.text.strip().lower()
    if field not in fields:
        logger.warning(
            "User %s selected invalid edit field '%s'",
            message.from_user.id,
            field,
        )
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

    logger.info(
        "User %s selected field '%s' for cocktail '%s'",
        message.from_user.id,
        field,
        name,
    )

    try:
        cocktail_id = await asyncio.to_thread(update_cocktail_by_name, name, field, new_value)
    except Exception:
        logger.error(
            "Update failed for user %s (cocktail='%s', field='%s', value='%s')",
            message.from_user.id,
            name,
            field,
            new_value,
            exc_info=True,
        )
        await message.answer("Update failed")
        await state.clear()
        return
    if not cocktail_id:
        await message.answer("Update failed or cocktail not found")
        await state.clear()
        return
    logger.info(
        "User %s updated cocktail '%s': %s='%s' (id=%s)",
        message.from_user.id,
        name,
        field,
        new_value,
        cocktail_id,
    )
    await message.answer(f"{field.capitalize()} updated")
    await state.clear()