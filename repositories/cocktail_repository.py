from schemas.cocktail import CocktailCreate


#create cocktail db
def create_cocktail(conn, cocktail: CocktailCreate) ->int:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO cocktails (name, glass, garnish, method) VALUES (%s, %s, %s, %s) RETURNING id;", 
        (cocktail.name, cocktail.glass, cocktail.garnish, cocktail.method))
        row = cur.fetchone()
    return row["id"]
