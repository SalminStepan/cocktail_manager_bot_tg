# Этот файл содержит экспериментальный handler для ручной проверки добавления коктейля.
# Он лежит в tests как вспомогательный черновой сценарий и не подключается к production bot entrypoint.

from aiogram import Router, types
from aiogram.filters.command import Command
from services.cocktail_services import create_cocktail_with_ingredients
from schemas.cocktail import CocktailCreate
from schemas.ingredient import IngredientCreate

add_router = Router()

# Создает тестовый коктейль через сервисный слой по команде /add_test.
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
