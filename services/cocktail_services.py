# Этот файл содержит бизнес-сценарии работы с коктейлями поверх репозиториев.
# Он открывает соединения, собирает CocktailRead с ингредиентами и держит транзакции вне Telegram handlers.

from db.connection import get_connection
from repositories.cocktail_repository import (
    create_cocktail, 
    get_all_cocktails_names, 
    get_cocktail_by_name, 
    search_cocktails, 
    delete_cocktail, 
    update_cocktail,
    get_cocktail_by_id
)
from repositories.ingredient_repository import (
    create_ingredients, 
    get_ingredients_by_cocktail_id,
    delete_ingredients_by_cocktail_id)
from schemas.cocktail import CocktailCreate, CocktailRead
from schemas.ingredient import IngredientRead, IngredientCreate


# Создает коктейль и ингредиенты в одной транзакции.
def create_cocktail_with_ingredients(cocktail: CocktailCreate) -> int:
    with get_connection() as conn:
        cocktail_id = create_cocktail(conn, cocktail)
        create_ingredients(conn, cocktail_id, cocktail.ingredients)
        conn.commit()
        return cocktail_id

# Возвращает страницу коктейлей для /list.
def list_cocktails(page: int = 1) ->list[dict]:
    with get_connection() as conn:
        if page < 1:
            page = 1
        limit = 10
        offset = (page - 1) * limit
        cocktails = get_all_cocktails_names(conn, limit, offset)
        return cocktails
    
# Собирает полный CocktailRead по названию.
def get_full_cocktail_by_name(name: str) -> CocktailRead | None:
    with get_connection() as conn:
        cocktail = get_cocktail_by_name(conn, name)
        if not cocktail:
            return None
        cocktail_id = cocktail["id"]
        ingredients = get_ingredients_by_cocktail_id(conn, cocktail_id)
        ingredients_models = [
            IngredientRead(**ingredient)
            for ingredient in ingredients
        ]
        cocktail_model = CocktailRead(
            id=cocktail["id"],
            name=cocktail["name"],
            description=cocktail["description"],
            image_url=cocktail["image_url"],
            glass=cocktail["glass"],
            garnish=cocktail["garnish"],
            method=cocktail["method"],
            parse_status=cocktail["parse_status"],
            source_url=cocktail["source_url"],
            ingredients=ingredients_models,
            created_at=cocktail["created_at"]
        )
        return cocktail_model
    
# Собирает полный CocktailRead по id.
def get_full_cocktail_by_id(id: int) -> CocktailRead | None:
    with get_connection() as conn:
        cocktail = get_cocktail_by_id(conn, id)
        if not cocktail:
            return None
        cocktail_id = cocktail["id"]
        ingredients = get_ingredients_by_cocktail_id(conn, cocktail_id)
        ingredients_models = [
            IngredientRead(**ingredient)
            for ingredient in ingredients
        ]
        cocktail_model = CocktailRead(
            id=cocktail["id"],
            name=cocktail["name"],
            description=cocktail["description"],
            image_url=cocktail["image_url"],
            glass=cocktail["glass"],
            garnish=cocktail["garnish"],
            method=cocktail["method"],
            parse_status=cocktail["parse_status"],
            source_url=cocktail["source_url"],
            ingredients=ingredients_models,
            created_at=cocktail["created_at"]
        )
        return cocktail_model
    
# Возвращает страницу результатов поиска по строке пользователя.
def search_by_query(query: str, page: int = 1) -> list[dict]:
    with get_connection() as conn:
        if page < 1:
            page = 1
        limit = 10
        offset = (page - 1) * limit
        cocktails = search_cocktails(conn, query, limit, offset)
        return cocktails
    
# Удаляет коктейль по названию через repository layer.
def delete_cocktail_by_name(name: str) -> int | None:
    with get_connection() as conn:
        cocktail_id = delete_cocktail(conn, name)
        conn.commit()
        return cocktail_id
    
# Проверяет поле и обновляет коктейль по названию.
def update_cocktail_by_name(name: str, field: str, new_value: str) -> int | None:
    fields = {"glass", "garnish", "method"}
    if field not in fields:
        return None
    with get_connection() as conn:
        cocktail_id = update_cocktail(conn, name, field, new_value)
        if cocktail_id:
            conn.commit()
        return cocktail_id

# Полностью заменяет список ингредиентов коктейля.
def replace_cocktail_ingredients_by_name(
    name: str,
    ingredients: list[dict],
) -> int | None:
    with get_connection() as conn:
        cocktail = get_cocktail_by_name(conn, name)

        if not cocktail:
            return None

        cocktail_id = cocktail["id"]

        delete_ingredients_by_cocktail_id(conn, cocktail_id)

        ingredients_models = [IngredientCreate(**i) for i in ingredients]

        create_ingredients(conn, cocktail_id, ingredients_models)

        conn.commit()

        return cocktail_id
