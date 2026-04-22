from schemas.ingredient import IngredientCreate


#create ingredient into db
def create_ingredients(conn, cocktail_id: int, ingredients: list[IngredientCreate]) -> None:
    with conn.cursor() as cur:
        for ingredient in ingredients:
            cur.execute("""
                INSERT INTO ingredients 
                (cocktail_id, name, amount, unit, comment) 
                VALUES (%s, %s, %s, %s, %s);
                """, 
                (cocktail_id, ingredient.name, ingredient.amount, ingredient.unit, ingredient.comment))

def get_ingredients_by_cocktail_id(conn, cocktail_id: int) -> list[dict]:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, name, amount, unit, comment 
            FROM ingredients 
            WHERE cocktail_id = %s 
            ORDER BY id ASC;
            """, 
            (cocktail_id,))
        result = cur.fetchall()
        return result