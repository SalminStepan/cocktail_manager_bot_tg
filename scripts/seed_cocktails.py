from schemas.cocktail import CocktailCreate
from services.cocktail_services import create_cocktail_with_ingredients

cocktails_data = [
{
    "name": "Arnaud",
    "glass": "Cocktail glass",
    "garnish": "Blackberry",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Creme de Cassis", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Barracuda",
    "glass": "Cocktail glass",
    "garnish": "Pineapple",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum white", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Galliano Vanilla", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Pineapple Juise", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 7, "unit": "ml", "comment": None},
        {"name": "Prosecco", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Bellini",
    "glass": "Flute",
    "garnish": "Peach",
    "method": "Throwing",
    "ingredients": [
        {"name": "Peach Puree", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Prosecco", "amount": 100, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Between the sheets",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum white", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Cognac", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Tripple Sec", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Bijou",
    "glass": "Cocktail glass",
    "garnish": "Cherry",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Red", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Chartreuse Verte", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Orange Bitter", "amount": 1, "unit": "dash", "comment": None},
    ]
},
{
    "name": "Bees Knees",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Fuice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Honey Syrup", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Breakfast Martini",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Orange confiture", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Tripple Sec", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Brown Derby",
    "glass": "Cocktail glass",
    "garnish": "Grapefuit peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Grapefruit Juice", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Honey Syrup", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Bamboo",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Sherry Fino", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Orange Bitter", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Batanga",
    "glass": "Highball",
    "garnish": "Lime ring",
    "method": "Build",
    "ingredients": [
        {"name": "Tequila Silver", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Coca Cola", "amount_ml": 100, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Black Russian",
    "glass": "Rocks",
    "garnish": "No Garnish",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Kahlua", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Boulevardier",
    "glass": "Rocks",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Bourbon", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Red", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Campari Bitter", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Bramble",
    "glass": "Rocks",
    "garnish": "Blackberry",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juiice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Creme de Mure", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Sugar Syrup", "amount": 12, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Bloody Mary",
    "glass": "Highball",
    "garnish": "Celery",
    "method": "Stir",
    "ingredients": [
        {"name": "Vodka", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Tomato Juice", "amount": 90, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Worcestershire Sauce", "amount": 1, "unit": "dash", "comment": None},
        {"name": "Tabasco and spices", "amount": 1, "unit": "dash", "comment": None},
        {"name": "Salt", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Blood and Sand",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Whisky", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Red", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Cherry Brandy", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 25, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Bacardi",
    "glass": "Cocktail glass",
    "garnish": "No garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum Bacardi Blanca", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Grenadine syrup", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Bronx",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 7, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Red", "amount": 7, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Orange Bitter", "amount": 1, "unit": "dash", "comment": None},
    ]
},
{
    "name": "Casino",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Old Tom Gin", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Orange Bitter", "amount": 1, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Clover Club",
    "glass": "Cocktail glass",
    "garnish": "Fresh Raspberry",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Raspberry Syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 20, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Corpse Reviver #1",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Calvados", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Cognac", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Bianco", "amount": 25, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Corpse Reviver #2",
    "glass": "Cocktail glass",
    "garnish": "Absinthe",
    "method": "Shake",
    "ingredients": [
        {"name": "Absinthe", "amount": 5, "unit": "ml", "comment": "To rinse"},
        {"name": "Gin", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Lillet Blanc", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Tripple Sec", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Cosmopolitan",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Vodka Citron", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Cointreau", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "CranberryJuice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Orange Bitter", "amount": 25, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Cuba Libre",
    "glass": "Highball",
    "garnish": "Lime wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Rum", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Coca Cola", "amount": 100, "unit": "ml", "comment": None},
        {"name": "Fresh Lime", "amount": 35, "unit": "g", "comment": "Muddled"},
    ]
},
{
    "name": "Caipirinha",
    "glass": "Rocks",
    "garnish": "Lime wedge",
    "method": "Muddle",
    "ingredients": [
        {"name": "Cachaça", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Fresh Lime", "amount": 35, "unit": "g", "comment": "Muddled"},
        {"name": "Simple Syrup", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Canchanchara",
    "glass": "Rocks",
    "garnish": "Lime slice",
    "method": "Build",
    "ingredients": [
        {"name": "Rum White", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Honey Syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Soda Water", "amount": 15, "unit": "ml", "comment": "Splash"},
    ]
},
{
    "name": "Champagne Cocktail",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Build",
    "ingredients": [
        {"name": "Cognac", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sparkling Wine Brut", "amount": 100, "unit": "ml", "comment": None},
        {"name": "Sugar", "amount": 1, "unit": "cube", "comment": None},
    ]
},
{
    "name": "Cuzco",
    "glass": "Highball",
    "garnish": "Grapefruit peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Pisco", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Aperol", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Grapefruit Juice", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Sugar Syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Kirsch", "amount": 1, "unit": "dash", "comment": "Maraschino+Amaretto 4/1"},
    ]
},
{
    "name": "Churchill",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Whisky", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Red", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Tripple sec", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Daiquiri",
    "glass": "Cocktail glass",
    "garnish": "No garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum White", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Sugar Syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 20, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Dark'n'Stormy",
    "glass": "Cocktail glass",
    "garnish": "Lime wedge",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum BLack", "amount": 60, "unit": "ml", "comment": "On Top"},
        {"name": "Ginger Ale/Beer", "amount": 100, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 25, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Derby",
    "glass": "Cocktail glass",
    "garnish": "Fresh Mint",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Fresh Mint", "amount": 5, "unit": "pcs", "comment": None},
        {"name": "Peach Bitter", "amount": 25, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Dry Martini",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel / Olive",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 60, "unit": "ml", "comment": "or Vodka"},
        {"name": "Dry Vermouth", "amount": 15, "unit": "ml", "comment": "Full guide https://www.diffordsguide.com/g/1121/martini"},
        {"name": "Orange Bitter", "amount": 1, "unit": "dash", "comment": None},
    ]
},
{
    "name": "Espresso Martini",
    "glass": "Cocktail glass",
    "garnish": "Coffee beans",
    "method": "Shake",
    "ingredients": [
        {"name": "Vodka", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Kahlua", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Espresso", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sugar Syrup", "amount": 10, "unit": "ml", "comment": None},
    ]
},
{
    "name": "El Presidente",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Rum White", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Red", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Orange Curacao Liqueur", "amount": 10, "unit": "ml", "comment": "or Tripple Sec"},
        {"name": "Grenadine Syrup", "amount": 2, "unit": "dash", "comment": None},
    ]
},
{
    "name": "El Diablo",
    "glass": "Highball",
    "garnish": "Lime wedge",
    "method": "Shake",
    "ingredients": [
        {"name": "Tequila Reposado", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Creme de Cassis", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Ginger Ale / beer", "amount": 100, "unit": "ml", "comment": "on top"},
    ]
},
{
    "name": "Fernadito",
    "glass": "Highball",
    "garnish": "Lime wedge / no garnish",
    "method": "Build",
    "ingredients": [
        {"name": "Fernet Branca", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Coca Cola", "amount": 100, "unit": "ml", "comment": None},
    ]
},
{
    "name": "French 75",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Sugar Syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Sparkling Wine Brut", "amount": 60, "unit": "ml", "comment": "on top"},
    ]
},
{
    "name": "French Connection",
    "glass": "Rocks",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Cognac", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Amaretto", "amount": 30, "unit": "ml", "comment": None},
    ]
},
{
    "name": "French Martini",
    "glass": "Cocktail glass",
    "garnish": "Pineapple slice",
    "method": "Shake",
    "ingredients": [
        {"name": "Vodka", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Chambord", "amount": 15, "unit": "ml", "comment": "Creme de cassis(IBA)"},
        {"name": "Fresh Pineapple Juice", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Gimlet",
    "glass": "Cocktail glass",
    "garnish": "no garnish",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": "or lime cordial"},
        {"name": "Sugar syrup", "amount": 15, "unit": "ml", "comment": "or lime cordial"},
    ]
},
{
    "name": "Gibson",
    "glass": "Cocktail glass",
    "garnish": "Pickled Mini Onion",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Grasshopper",
    "glass": "Cocktail glass",
    "garnish": "Mint leave",
    "method": "Shake",
    "ingredients": [
        {"name": "Creme de Menthe", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Creme de Cacao white", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Cream", "amount": 30, "unit": "ml", "comment": "10-20%"},
    ]
},
{
    "name": "Golden Dream",
    "glass": "Cocktail glass",
    "garnish": "No garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Galliano Vanilla", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Cointreau", "amount": 25, "unit": "ml", "comment": "or Trippke Sec"},
        {"name": "Cream", "amount": 25, "unit": "ml", "comment": "10-20%"},
        {"name": "Fresh Orange Juice", "amount": 25, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Golden Cadillac",
    "glass": "Cocktail glass",
    "garnish": "No garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Galliano Vanilla", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Creme de Cacao white", "amount": 25, "unit": "ml", "comment": "or Trippke Sec"},
        {"name": "Cream", "amount": 25, "unit": "ml", "comment": "10-20%"},
    ]
},
{
    "name": "Gin Fizz",
    "glass": "Highball",
    "garnish": "No garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Soda Water", "amount": 30, "unit": "ml", "comment": "on top"},
    ]
},
{
    "name": "God Father",
    "glass": "Rocks",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Whisky", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Amaretto", "amount": 30, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Gin Basil Smash",
    "glass": "Rocks",
    "garnish": "Basil leaves",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Frash Basil Leaves", "amount": 7, "unit": "g", "comment": None},
        {"name": "Sugar Syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Gin Tonic",
    "glass": "Highball",
    "garnish": "Lime wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Gin", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Tonic", "amount": 25, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Hanky Panky",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Red", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fernet Branca", "amount": 2, "unit": "dash", "comment": None},
    ]
},
{
    "name": "Hemingway special",
    "glass": "Cocktail glass",
    "garnish": "Maraschino cherry",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum White", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 5, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Fresh Grapefriut Juice", "amount": 20, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Horse's Neck",
    "glass": "Highball",
    "garnish": "Lemon peel",
    "method": "Build",
    "ingredients": [
        {"name": "Bourbon", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Ginger Ale /  Beer", "amount": 100, "unit": "ml", "comment": None},
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