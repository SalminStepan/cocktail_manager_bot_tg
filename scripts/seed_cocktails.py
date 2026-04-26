from schemas.cocktail import CocktailCreate
from services.cocktail_services import create_cocktail_with_ingredients

cocktails_data = [
{
    "name": "Adonis",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Sherry Fino", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Orange Bitter", "amount": 2, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Alexander",
    "glass": "Cocktail glass",
    "garnish": "Nutmeg",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Creme de Cacao", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Cream", "amount": 30, "unit": "ml", "comment": "10-20%"}
    ]
},
{
    "name": "Americano",
    "glass": "Highball",
    "garnish": "Orange wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Bitter Campari", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Soda Water", "amount": 80, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Angel Face",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Apricot brandy", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Calvados", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Aviation",
    "glass": "Cocktail glass",
    "garnish": "Cherry",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Creme de voilette", "amount": 5, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Allies",
    "glass": "Cocktail glass",
    "garnish": "No garnish",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Kummel", "amount": 2, "unit": "dash", "comment": None},
        {"name": "Honey Syrup", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Alaska",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin Old Tom", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Chartreuse jaune", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Orange bitter", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Affinity",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Whisky", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Angostura bitter", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Amaretto sour",
    "glass": "Rocks",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Amaretto", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Apple Jack",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Sweet Vermouth Red", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Laird's Applejack", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Angostura bitter", "amount_ml": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Apple Jack Rabbit",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Calvados", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Marple syrup", "amount": 15, "unit": "ml", "comment": None}

    ]
},
{
    "name": "Bijou",
    "glass": "Cocktail glass",
    "garnish": "Cherry",
    "method": "Shake",
    "ingredients": [
        {"name": "Cognac", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Campari Bitter", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Batanga",
    "glass": "Highball",
    "garnish": "Lime wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Tequila Silver", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Coca Cola", "amount": 100, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Brandy Crusta",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Brandy", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 5, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Angostura Bitter", "amount": 2, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Harvey Wallbanger",
    "glass": "Highball",
    "garnish": "Orange wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Galliano Vanilla", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 90, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Hugo",
    "glass": "Rocks",
    "garnish": "Fresh mint",
    "method": "Build",
    "ingredients": [
        {"name": "Sparkling Wine", "amount": 60, "unit": "ml", "comment": None},
        {"name": "St-Germain", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Soda Water", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Mint Leaves", "amount": 8, "unit": "pcs", "comment": None}
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
        {"name": "Sweet Vermouth Rosso", "amount": 7, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Orange Bitter", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Irish Coffee",
    "glass": "Cocktail glass",
    "garnish": "Coffee",
    "method": "Shake",
    "ingredients": [
        {"name": "Whisky", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Americano Coffee", "amount": 120, "unit": "ml", "comment": "Hot"},
        {"name": "Sugar", "amount": 2, "unit": "g", "comment": None},
        {"name": "Whipped cream", "amount": 1, "unit": "ml", "comment": "On top"}
    ]
},
{
    "name": "Illegal	",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Mezcal", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Rum White", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Falernum Syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "John Collins",
    "glass": "Highball",
    "garnish": "Lemon wedge",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Soda Water", "amount": 50, "unit": "ml", "comment": "On top"}
    ]
},
{
    "name": "Jungle Bird",
    "glass": "Rocks",
    "garnish": "Pineapple",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum Black", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Bitter Campari", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Pineapple Juice", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Demerara syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Jack Rose",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Laird's Applejack", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Grenadine syrup", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "KIR",
    "glass": "Wine Glass",
    "garnish": "No garnish",
    "method": "Build",
    "ingredients": [
        {"name": "White wine dry", "amount": 90, "unit": "ml", "comment": "Use Sparkling Wine for KIR ROYALE"},
        {"name": "Creme de Cassis", "amount": 10, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Kamikaze",
    "glass": "Cocktail glass",
    "garnish": "Lime wedge",
    "method": "Shake",
    "ingredients": [
        {"name": "Vodka", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Triple sec", "amount": 20, "unit": "ml", "comment": "Muddled"},
        {"name": "Fresh Lime Juice", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Knickerbocker",
    "glass": "Rocks",
    "garnish": "Raspberry",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum White", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Orage quracao", "amount": 5, "unit": "ml", "comment": None},
        {"name": "Raspberry syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Lemon Drop Martini",
    "glass": "Cocktail glass",
    "garnish": "Sugar crust",
    "method": "Stir",
    "ingredients": [
        {"name": "Vodka Citron", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "cube", "comment": None}
    ]
},
{
    "name": "Long Island Iced Tea",
    "glass": "Highball",
    "garnish": "Lemon wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Rum White", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Tequila Silver", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Gin", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Coca Cola", "amount": 50, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Last Word",
    "glass": "Cocktail glass",
    "garnish": "Lime peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Chartreuse  Jaune", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Mai-Tai",
    "glass": "Rocks",
    "garnish": "Mint, Lime peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum White", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Rum Black", "amount": 30, "unit": "ml", "comment": "On top"},
        {"name": "Orange Curacao", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Orgeat Syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 25, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Manhattan",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Bourbon", "amount": 60, "unit": "ml", "comment": "Or Rye"},
        {"name": "Sweet Vermouth Rosso", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Angostura Bitter", "amount": 2, "unit": "dash", "comment": None}
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
        {"name": "Peach Bitter", "amount": 2, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Mary Pickford",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel / Olive",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum White", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Pineapple Juice", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 5, "unit": "ml", "comment": None},
        {"name": "Grenadine syrup", "amount": 5, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Margarita",
    "glass": "Cocktail glass",
    "garnish": "Lime wedge",
    "method": "Shake",
    "ingredients": [
        {"name": "Tequila Silver", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Martinez",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Orange bitter", "amount": 2, "unit": "dash", "comment": None},
    ]
},
{
    "name": "Mint Julep",
    "glass": "Copper mug",
    "garnish": "Mint",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Fresh Mint Leaves", "amount": 10, "unit": "pcs", "comment": None},
        {"name": "Sugar syrup", "amount": 10, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Mimosa",
    "glass": "Highball",
    "garnish": "No garnish",
    "method": "Build",
    "ingredients": [
        {"name": "Fresh Orange Juice", "amount": 75, "unit": "ml", "comment": None},
        {"name": "Sparkling Wine", "amount": 75, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Mojito",
    "glass": "Highball",
    "garnish": "Mint, Lime wedge",
    "method": "Muddle",
    "ingredients": [
        {"name": "Rum White", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Lime", "amount": 35, "unit": "g", "comment": "Muddled"},
        {"name": "Sugar Syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Mint Leaves", "amount": 14, "unit": "pcs", "comment": None}
    ]
},
{
    "name": "Monkey Gland",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Absinthe", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Grenadine syrup", "amount": 1, "unit": "bspn", "comment": None}
    ]
},
{
    "name": "Moscow Mule",
    "glass": "Copper mug",
    "garnish": "Mint, Lime wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Ginger Ale", "amount": 120, "unit": "ml", "comment": "or Ginger Beer"},
        {"name": "Fresh Lime Juice", "amount": 10, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Naked and Famous",
    "glass": "Cocktail glass",
    "garnish": "No garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Mezcal", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Aperol", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Chartreuse  Jaune", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Negroni",
    "glass": "Rocks",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Campari", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{#stop here
    "name": "Negroni Sbagliato",
    "glass": "Rocks",
    "garnish": "Orange peel",
    "method": "Build",
    "ingredients": [
        {"name": "Campari", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Sparkling Wine", "amount": 30, "unit": "ml", "comment": None},
    ]
},
{
    "name": "New York Sour",
    "glass": "Rocks",
    "garnish": "No garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Egg white", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Red Dry Wine", "amount": 25, "unit": "ml", "comment": "On top"},
    ]
},
{
    "name": "Old Fashioned",
    "glass": "Rocks",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Bourbon", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Angostura Bitter", "amount": 3, "unit": "dash", "comment": None},
    ]
},
{
    "name": "Old Pal",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Rye Whisky", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Capmari Bitter", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Old Cuban",
    "glass": "Cocktail glass",
    "garnish": "Mint",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum Aged", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Mint Meaves", "amount": 10, "unit": "pcs", "comment": None},
        {"name": "Sparkling Wine", "amount": 30, "unit": "ml", "comment": "On top"}
    ]
},
{
    "name": "Old Flame",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Campari Bitter", "amount": 7, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 45, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Paloma",
    "glass": "Highball",
    "garnish": "Grapefruit wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Tequila", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 5, "unit": "ml", "comment": None},
        {"name": "Salt", "amount": 5, "unit": "g", "comment": "To crust"},
        {"name": "Pink Grapefruit Soda", "amount": 100, "unit": "ml", "comment": None},

    ]
},
{
    "name": "Paper Plane",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Aperol", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Amaro", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Paradise",
    "glass": "Cocktail glass",
    "garnish": "No Garnish",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Apricot Brandy", "amount": 5, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 10, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Pegu Club",
    "glass": "Cocktail glass",
    "garnish": "Lime peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Orange Curacao", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Angostura Bitter", "amount": 1, "unit": "dash", "comment": None},
        {"name": "Orange bitter", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Pisco Sour",
    "glass": "Cocktail glass",
    "garnish": "Angostura bitter drop",
    "method": "Shake",
    "ingredients": [
        {"name": "Pisco", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Planter's Punch",
    "glass": "Cocktail glass",
    "garnish": "Lime peel",
    "method": "Long stir on the glass",
    "ingredients": [
        {"name": "Jamaican Rum", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Sugar Cane Juice", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Penicillin",
    "glass": "Rocks",
    "garnish": "Candied ginger",
    "method": "Shake",
    "ingredients": [
        {"name": "Whisky Blended", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Singe Malt Wisky", "amount": 5, "unit": "ml", "comment": "Islay, on top"},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Honey syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Ginger", "amount": 10, "unit": "g", "comment": "Muddled"}
    ]
},
{
    "name": "Porn Star Martini",
    "glass": "Cocktail glass",
    "garnish": "Passionfruit",
    "method": "Shake",
    "ingredients": [
        {"name": "Vodka Vanilla", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Passionfruit Puree", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Passion Fruit Liqueur", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Vanilla syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Sparkling Wine", "amount": 60, "unit": "ml", "comment": "On top"}
    ]
},
{
    "name": "Porto Flip",
    "glass": "Cocktail glass",
    "garnish": "Nutmeg",
    "method": "Shake",
    "ingredients": [
        {"name": "Brandy", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Port Wine Tawny", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Egg Yolk", "amount": 10, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Pina Colada",
    "glass": "Tiki Mug",
    "garnish": "Pineapple",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum White", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Coconut Cream", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Fresh Pineapple Juice", "amount": 50, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Pink Lady",
    "glass": "Cocktail glass",
    "garnish": "Cherry",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Applejack", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Grenadine syrup", "amount": 7, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Painkiller",
    "glass": "Hurricane",
    "garnish": "Nutmeg",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum", "amount": 60, "unit": "ml", "comment": None},
        {"name": "Fresh Pineapple Juice", "amount": 120, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Coconut Cream", "amount": 30, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Ramos Gin Fizz",
    "glass": "Highball",
    "garnish": "Lime peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "bspn", "comment": None},
        {"name": "Sugar syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Cream", "amount": 30, "unit": "ml", "comment": "10-20%"},
        {"name": "Egg White", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Orange water", "amount": 3, "unit": "dash", "comment": None},
        {"name": "Vanilla extract", "amount": 2, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Revolver",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Whisky", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Kahlua", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Orange bitter", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Rob Roy",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Whisky", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Sweet Vermouth Rosso", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Orange bitter", "amount": 2, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Rose",
    "glass": "Cocktail glass",
    "garnish": "Cherry",
    "method": "Stir",
    "ingredients": [
        {"name": "Kirsch", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Strawberry Syrup", "amount": 3, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Rusty Nail",
    "glass": "Rocks",
    "garnish": "No garnish",
    "method": "Stir",
    "ingredients": [
        {"name": "Whisky", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Drambuie", "amount": 25, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Russian Spring Punch",
    "glass": "Highball",
    "garnish": "Blackberry",
    "method": "Shake",
    "ingredients": [
        {"name": "Vodka", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Creme de Cassis", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Spakling Wine", "amount": 50, "unit": "ml", "comment": "On top"}
    ]
},
{
    "name": "Sazerac",
    "glass": "Rocks",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Cognac", "amount": 50, "unit": "ml", "comment": "Or Rye Whisky"},
        {"name": "Absinthe", "amount": 10, "unit": "ml", "comment": "To rinse"},
        {"name": "Peychard's Bitter", "amount": 2, "unit": "dash", "comment": None},
        {"name": "Sugar", "amount": 2, "unit": "g", "comment": "or sugar syrup"}
    ]
},
{
    "name": "Sidecar",
    "glass": "Cocktail glass",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Cognac", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Screwdriver",
    "glass": "Highball",
    "garnish": "Orange wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 100, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Southside",
    "glass": "Cocktail glass",
    "garnish": "Mint",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Fresh Mint Leaves", "amount": 10, "unit": "pcs", "comment": None}
    ]
},
{
    "name": "Stinger",
    "glass": "Rocks",
    "garnish": "No garnish",
    "method": "Stir",
    "ingredients": [
        {"name": "Cognac", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Creme de Menthe", "amount": 20, "unit": "ml", "comment": "Or Branca Menthe"}
    ]
},
{
    "name": "Sea Breeze",
    "glass": "Highball",
    "garnish": "Lime wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Cranberry Juice", "amount": 120, "unit": "ml", "comment": None},
        {"name": "Fresh Grapefruit Juice", "amount": 30, "unit": "ml", "comment": None}
    ]
},

{
    "name": "Sex On The Beach",
    "glass": "Highball",
    "garnish": "No garnish",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Peach Schnapps", "amount": 20, "unit": "ml", "comment": "Or Peach Tree Liqueur"},
        {"name": "Cranberry Juice", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 40, "unit": "ml", "comment": None}
    ]
},
{
    "name": "Singapore Sling",
    "glass": "Tiki Mug / Sling",
    "garnish": "Bamboo leave",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Cointreau", "amount": 7, "unit": "ml", "comment": None},
        {"name": "DOM Benedictine", "amount": 7, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Pineapple Juice", "amount": 120, "unit": "ml", "comment": None},
        {"name": "Grenadine syrup", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Angostura Bitter", "amount": 1, "unit": "dash", "comment": None}
    ]
},
{
    "name": "Tuxedo",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin Old Tom", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Dry Vermouth", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Maraschino", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Absinthe", "amount": 5, "unit": "ml", "comment": "To rinse"},
        {"name": "Orange Bitter", "amount": 2, "unit": "dash", "comment": None}
        
    ]
},
{
    "name": "Tequila Sunrise",
    "glass": "Highball",
    "garnish": "Orange wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Tequila Silver", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Fresh Orange Juice", "amount": 90, "unit": "ml", "comment": None},
        {"name": "Grenadine syrup", "amount": 15, "unit": "ml", "comment": "last"}
    ]
},
{
    "name": "Tiramisu",
    "glass": "Cocktail glass",
    "garnish": "Chocolate shavings",
    "method": "Shake",
    "ingredients": [
        {"name": "Cognac", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Kahlua", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Creme de Cacao brown", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Cream", "amount": 30, "unit": "ml", "comment": "10-20%"},
        {"name": "Egg Yolk", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Mascarpone", "amount": 3, "unit": "bspn", "comment": None},
    ]
},
{
    "name": "Tom Collins",
    "glass": "Highball",
    "garnish": "Lemon wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Gin Old Tom", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Soda Water", "amount": 50, "unit": "ml", "comment": None},

    ]
},
{
    "name": "Vesper",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Stir",
    "ingredients": [
        {"name": "Gin", "amount": 45, "unit": "ml", "comment": None},
        {"name": "Lillet Blanc", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Vodka", "amount": 15, "unit": "ml", "comment": None}
    ]
},
{
    "name": "VE.N.T.O",
    "glass": "Rocks",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Grappa", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Chamomile Cordial", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Honey mix", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Whiskey Sour",
    "glass": "Highball",
    "garnish": "Orange peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Bourbon", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 25, "unit": "ml", "comment": None},
        {"name": "Sugar syrup", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Egg White", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "White Lady",
    "glass": "Cocktail glass",
    "garnish": "Lemon peel",
    "method": "Shake",
    "ingredients": [
        {"name": "Gin", "amount": 40, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Fresh Lemon Juice", "amount": 20, "unit": "ml", "comment": None}
    ]
},
{
    "name": "White Russian",
    "glass": "Rocks",
    "garnish": "No garnish",
    "method": "Build",
    "ingredients": [
        {"name": "Vodka", "amount": 50, "unit": "ml", "comment": None},
        {"name": "Kahlua", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Cream", "amount": 30, "unit": "ml", "comment": "10-20%"}
    ]
},
{
    "name": "Yellow bird",
    "glass": "Cocktail glass",
    "garnish": "Baboo leaves",
    "method": "Shake",
    "ingredients": [
        {"name": "Rum White", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Galliano Vanilla", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Triple Sec", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Fresh Lime Juice", "amount": 15, "unit": "ml", "comment": None},
    ]
},
{
    "name": "Zombie",
    "glass": "Highball",
    "garnish": "Lime wedge",
    "method": "Build",
    "ingredients": [
        {"name": "Rum Gold", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Rum White", "amount": 30, "unit": "ml", "comment": None},
        {"name": "Rum Overproof", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Falernum syrup", "amount": 15, "unit": "ml", "comment": None},
        {"name": "Cinnamon syrup", "amount": 10, "unit": "ml", "comment": None},
        {"name": "Grenadine syrup", "amount": 1, "unit": "bspn", "comment": None},
        {"name": "Fresh Grapefruit Juice", "amount": 20, "unit": "ml", "comment": None},
        {"name": "Angostura Bitter", "amount": 1, "unit": "dash", "comment": None},
        {"name": "Pernod", "amount": 6, "unit": "dash", "comment": None}

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