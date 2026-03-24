from schemas.cocktail import CocktailCreate
from services.cocktail_services import create_cocktail_with_ingredients

cocktails_data = [
{
    "name": "Alaska",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin Old Tom", "amount_ml": 50},
        {"name": "Chartreuse Jaune", "amount_ml": 20},
        {"name": "Orange Bitter", "amount_ml": 1}
    ]
},
{
    "name": "Allies",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel/No garnish",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount_ml": 30},
        {"name": "Dry Vermouth", "amount_ml": 30},
        {"name": "Kummel", "amount_ml": 1}
    ]
},
{
    "name": "Affinity",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Whisky", "amount_ml": 30},
        {"name": "Sweet Vermouth", "amount_ml": 30},
        {"name": "Dry Vermouth", "amount_ml": 30},
        {"name": "Angostura Bitter", "amount_ml": 1}
    ]
},
{
    "name": "Amaretto Sour",
    "glass": "Rocks",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount_ml": 45},
        {"name": "Amaretto", "amount_ml": 20},
        {"name": "Fresh lemon", "amount_ml": 20},
        {"name": "Egg White", "amount_ml": 15}
    ]
},
{
    "name": "Apple jack",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Sweet Vermouth", "amount_ml": 60},
        {"name": "Laird's Applejack", "amount_ml": 30},
        {"name": "Angostura Bitter", "amount_ml": 1}
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