# Этот файл содержит SQL-запросы к таблице ingredients.
# Он вынесен отдельно, потому что ингредиенты живут как дочерние записи коктейля и обновляются отдельными операциями.

from schemas.ingredient import IngredientCreate


# Создает ингредиенты для указанного коктейля.
def create_ingredients(conn, cocktail_id: int, ingredients: list[IngredientCreate]) -> None:
    with conn.cursor() as cur:
        for ingredient in ingredients:
            cur.execute("""
                INSERT INTO ingredients 
                (cocktail_id, name, amount, unit, comment) 
                VALUES (%s, %s, %s, %s, %s);
                """, 
                (cocktail_id, ingredient.name, ingredient.amount, ingredient.unit, ingredient.comment))

# Возвращает ингредиенты коктейля в порядке позиции.
def get_ingredients_by_cocktail_id(conn, cocktail_id: int) -> list[dict]:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, position, raw, amount, unit, name, comment, unresolved 
            FROM ingredients 
            WHERE cocktail_id = %s 
            ORDER BY position ASC;
            """, 
            (cocktail_id,))
        result = cur.fetchall()
        return result

# Удаляет все ингредиенты указанного коктейля.
def delete_ingredients_by_cocktail_id(conn, cocktail_id: int) -> None:
    with conn.cursor() as cur:
        cur.execute(
        "DELETE FROM ingredients WHERE cocktail_id = %s;", 
        (cocktail_id, )
        )
