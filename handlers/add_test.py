from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import create_cocktail_with_ingredients
from schemas.cocktail import CocktailCreate
from schemas.ingredient import IngredientCreate

#router
add_router = Router()

@add_router.message(Command("add_test"))
async def add_test(message:types.Message):
    cocktail = CocktailCreate(
        name = "",
        glass = "",
        garnish = "",
        method = "",
        ingredients = [IngredientCreate()
        ]
    )
    cocktail_id = create_cocktail_with_ingredients(cocktail)
    await message.answer(f"Cocktail created with id: {cocktail_id}")