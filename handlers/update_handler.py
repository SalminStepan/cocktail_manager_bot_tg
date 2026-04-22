from aiogram import Router, types
from aiogram.filters.command import Command
from schemas.cocktail import CocktailCreate
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.cocktail_services import update_cocktail_by_name
from config import ADMIN_IDS

update_router = Router()
@update_router.message(Command("edit"))
async def cocktail_handler(message:types.Message):
    pass