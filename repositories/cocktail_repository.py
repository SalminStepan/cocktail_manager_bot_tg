from schemas.cocktail import CocktailCreate


#create cocktail db
def create_cocktail(conn, cocktail: CocktailCreate) ->int:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO cocktails (name, glass, garnish, method) VALUES (%s, %s, %s, %s) RETURNING id;", 
        (cocktail.name, cocktail.glass, cocktail.garnish, cocktail.method))
        row = cur.fetchone()
    return row["id"]

def get_all_cocktails_names(conn) -> list:
    with conn.cursor() as cur:
        cur.execute("SELECT name FROM cocktails ORDER BY id LIMIT 20;")
        result = cur.fetchall()
        return result

def get_cocktail_by_name(conn, name) -> dict | None:
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, glass, garnish, method, created_at FROM cocktails WHERE name = %s;", (name,))
        result = cur.fetchone()
        return result