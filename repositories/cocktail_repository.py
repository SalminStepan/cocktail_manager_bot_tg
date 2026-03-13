from ..schemas.cocktail import CocktailCreate
from ..db.connection import get_connection


def create_cocktail(cocktail: CocktailCreate) ->int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO cocktails (name, glass, garnish, method) VALUES (%s, %s, %s, %s) RETURNING id;", 
            (cocktail.name, cocktail.glass, cocktail.garnish, cocktail.method))
            row = cur.fetchone()
        conn.commit() 
    return row["id"]
