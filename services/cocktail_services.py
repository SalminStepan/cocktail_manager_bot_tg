from db.connection import get_connection
from repositories.cocktail_repository import create_cocktail, get_all_cocktails_names, get_cocktail_by_name, search_cocktails, delete_cocktail
from repositories.ingredient_repository import create_ingredients, get_ingredients_by_cocktail_id
from schemas.cocktail import CocktailCreate, CocktailRead
from schemas.ingredient import IngredientRead


# Create cocktail with ingredients in single transaction
def create_cocktail_with_ingredients(cocktail: CocktailCreate) -> int:
    with get_connection() as conn:
        cocktail_id = create_cocktail(conn, cocktail)
        create_ingredients(conn, cocktail_id, cocktail.ingredients)
        conn.commit()
        return cocktail_id

def list_cocktails(page: int = 1) ->list[dict]:
    with get_connection() as conn:
        if page<1:
            page = 1
        limit = 20
        offset = (page - 1)*limit
        cocktails = get_all_cocktails_names(conn, limit, offset)
        return cocktails
    
def get_full_cocktail_by_name(name) -> CocktailRead | None:
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
            glass=cocktail["glass"],
            garnish=cocktail["garnish"],
            method=cocktail["method"],
            created_at=cocktail["created_at"],
            ingredients=ingredients_models
        )
        return cocktail_model
    
def search_by_query(query) -> list[dict]:
    with get_connection() as conn:
        cocktails = search_cocktails(conn, query)
        return cocktails
    
def delete_cocktail_by_name(name) -> int | None:
    with get_connection() as conn:
        cocktail_id = delete_cocktail(conn, name)
        conn.commit()
        return cocktail_id