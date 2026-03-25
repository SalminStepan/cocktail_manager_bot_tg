from schemas.cocktail import CocktailCreate


#create cocktail db
def create_cocktail(conn, cocktail: CocktailCreate) ->int:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO cocktails (name, glass, garnish, method) VALUES (%s, %s, %s, %s) RETURNING id;", 
        (cocktail.name, cocktail.glass, cocktail.garnish, cocktail.method))
        row = cur.fetchone()
    return row["id"]

def get_all_cocktails_names(conn, limit, offset) -> list[dict]:
    with conn.cursor() as cur:
        cur.execute("SELECT name FROM cocktails ORDER BY id LIMIT %s OFFSET %s;", (limit, offset))
        result = cur.fetchall()
        return result

def get_cocktail_by_name(conn, name) -> dict | None:
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, glass, garnish, method, created_at FROM cocktails WHERE name = %s;", (name,))
        result = cur.fetchone()
        return result

def search_cocktails(conn, query) -> list[dict]:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT DISTINCT c.id, c.name
            FROM cocktails c
            LEFT JOIN ingredients i ON c.id = i.cocktail_id
            WHERE c.name ILIKE %s
               OR i.name ILIKE %s
            ORDER BY c.id;
        """, (f"%{query}%", f"%{query}%"))
        return cur.fetchall()
    
def delete_cocktail(conn, name) -> int | None:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM cocktails WHERE name = %s RETURNING id", (name,))
        row = cur.fetchone()
    if row:
        return row["id"]
    return None