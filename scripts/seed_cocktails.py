from schemas.cocktail import CocktailCreate
from services.cocktail_services import create_cocktail_with_ingredients

cocktails_data = [
{
    "name": "Arnaud",
    "glass": "Cocktail glass",
    "garnish": "Blackberry",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount_ml": 30},
        {"name": "Dry Vermouth", "amount_ml": 30},
        {"name": "Creme de Cassis", "amount_ml": 30}
    ]
},
{
    "name": "Barracuda",
    "glass": "Cocktail glass",
    "garnish": "Pineapple",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum white", "amount_ml": 45},
        {"name": "Galliano Vanilla", "amount_ml": 15},
        {"name": "Fresh Pineapple Juise", "amount_ml": 45},
        {"name": "Fresh Lime Juice", "amount_ml": 7},
        {"name": "Prosecco", "amount_ml": 30}
    ]
},
{
    "name": "Bellini",
    "glass": "Flute",
    "garnish": "Peach",
    "method": "Throwing",
    "ingredients": [
        {"name": "Peach Puree", "amount_ml": 50},
        {"name": "Prosecco", "amount_ml": 100}
    ]
},
{
    "name": "Between the sheets",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum white", "amount_ml": 30},
        {"name": "Cognac", "amount_ml": 30},
        {"name": "Tripple Sec", "amount_ml": 30},
        {"name": "Fresh Lemon Juice", "amount_ml": 15}
    ]
},
{
    "name": "Bijou",
    "glass": "Cocktail glass",
    "garnish": "Cherry",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount_ml": 30},
        {"name": "Sweet Vermouth", "amount_ml": 30},
        {"name": "Chartreuse Verte", "amount_ml": 30},
        {"name": "Orange Bitter", "amount_ml": 1},
    ]
},
{
    "name": "Bees Knees",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount_ml": 50},
        {"name": "Fresh Lemon Juice", "amount_ml": 20},
        {"name": "Fresh Orange Fuice", "amount_ml": 20},
        {"name": "Honey Syrup", "amount_ml": 15},
    ]
},
{
    "name": "Breakfast Martini",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount_ml": 45},
        {"name": "Orange confiture", "amount_ml": 30},
        {"name": "Tripple Sec", "amount_ml": 15},
        {"name": "Fresh Lime Juice", "amount_ml": 15},
    ]
},
{
    "name": "Brown Derby",
    "glass": "Cocktail glass",
    "garnish": "Grapefuit peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount_ml": 45},
        {"name": "Fresh Grapefruit Juice", "amount_ml": 30},
        {"name": "Honey Syrup", "amount_ml": 15}
    ]
},
{
    "name": "Bamboo",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Sherry Fino", "amount_ml": 45},
        {"name": "Dry Vermouth", "amount_ml": 45},
        {"name": "Orange Bitter", "amount_ml": 1}
    ]
},
{
    "name": "Batanga",
    "glass": "Highball",
    "garnish": "Lime ring",
    "method": "Build",
    "ingredients": [
        {"name": "Tequila Silver", "amount_ml": 45},
        {"name": "Fresh Lime Juice", "amount_ml": 15},
        {"name": "Coka Cola", "amount_ml": 100}
    ]
},
{
    "name": "Black Russian",
    "glass": "Rocks",
    "garnish": "No Garnish",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount_ml": 50},
        {"name": "Kahlua", "amount_ml": 20}
    ]
},
{
    "name": "Boulevardier",
    "glass": "Rocks",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Bourbon", "amount_ml": 40},
        {"name": "Sweet Vermouth", "amount_ml": 30},
        {"name": "Bitter", "amount_ml": 30}
    ]
},
{
    "name": "Bramble",
    "glass": "Rocks",
    "garnish": "Blackberry",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount_ml": 45},
        {"name": "Fresh Lemon Juiice", "amount_ml": 25},
        {"name": "Creme de Mure", "amount_ml": 15},
        {"name": "Sugar Syrup", "amount_ml": 12},
    ]
},
{
    "name": "Bloody Mary",
    "glass": "Highball",
    "garnish": "Celery",
    "method": "Stir",
    "ingredients": [
        {"name": "Vodka", "amount_ml": 45},
        {"name": "Tomato Juice", "amount_ml": 90},
        {"name": "Fresh Lemon Juice", "amount_ml": 15},
        {"name": "Worcestershire Sauce", "amount_ml": 1},
        {"name": "Tabasco and spices", "amount_ml": 1},
        {"name": "Salt", "amount_ml": 1}
    ]
},
{
    "name": "Blood and Sand",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Whisky", "amount_ml": 25},
        {"name": "Sweet Vermouth", "amount_ml": 25},
        {"name": "Cherry Brandy", "amount_ml": 25},
        {"name": "Fresh Orange Juice", "amount_ml": 25},
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