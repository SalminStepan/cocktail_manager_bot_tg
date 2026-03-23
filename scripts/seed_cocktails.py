from schemas.cocktail import CocktailCreate
from services.cocktail_services import create_cocktail_with_ingredients

cocktails_data = [
{
    "name": "Adonis",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Sherry Fino", "amount_ml": 45},
        {"name": "Sweet Vermouth", "amount_ml": 45},
        {"name": "Orange Bitter", "amount_ml": 1}
    ]
},
{
    "name": "Alexander",
    "glass": "Cocktail glass",
    "garnish": "Nutmeg Powder",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount_ml": 30},
        {"name": "Creme de Cacao", "amount_ml": 30},
        {"name": "Cream", "amount_ml": 30}
    ]
},
{
    "name": "Americano",
    "glass": "Highball",
    "garnish": "Orange slice",
    "method": "Build",
    "ingredients": [
        {"name": "Campari", "amount_ml": 30},
        {"name": "Sweet Vermouth", "amount_ml": 30},
        {"name": "Soda Water", "amount_ml": 80}
    ]
},
{
    "name": "Angel Face",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount_ml": 30},
        {"name": "Apricot Brandy", "amount_ml": 30},
        {"name": "Calvados", "amount_ml": 30}
    ]
},
{
    "name": "Aviation",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel/Maraschino Cherry",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount_ml": 45},
        {"name": "Maraschino", "amount_ml": 15},
        {"name": "Fresh lemon", "amount_ml": 30},
        {"name": "Creme de Violette", "amount_ml": 5}
    ]
},
]

def seed_cocktails(cocktails_data:list[dict]) -> None:
    for cocktail_dict in cocktails_data:
        try:
            cocktail = CocktailCreate(**cocktail_dict)
            cocktail_id = create_cocktail_with_ingredients(cocktail)
            print(f"Added: {cocktail.name} (id: {cocktail_id})")
        except Exception as e:
            print(f"Skipped: {cocktail_dict['name']}. Error: {e}")

if __name__ == "__main__":
    seed_cocktails(cocktails_data)