from db.connection import get_connection
from repositories.cocktail_repository import create_cocktail
from repositories.ingredient_repository import create_ingredients
from schemas.cocktail import CocktailCreate

# Create cocktail with ingredients in single transaction
def create_cocktail_with_ingredients(cocktail: CocktailCreate) -> int:
    with get_connection() as conn:
        cocktail_id = create_cocktail(conn, cocktail)
        create_ingredients(conn, cocktail_id, cocktail.ingredients)
        conn.commit()
        return cocktail_id
