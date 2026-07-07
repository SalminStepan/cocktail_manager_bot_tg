from utils.ingredient_formatter import format_ingredient
from schemas.cocktail import CocktailRead


def format_cocktail_text(cocktail: CocktailRead) -> str:
    cocktail_text = [f"🍸 {cocktail.name}",""]
    
    if cocktail.glass is not None:
        cocktail_text.append(f"Glass: {cocktail.glass}")
    else:
        cocktail_text.append("Glass: not specified")
        
    if cocktail.method is not None:
        cocktail_text.append(f"Method: {cocktail.method}")
    else:
        cocktail_text.append("Method: not specified")

    if cocktail.garnish is not None:
        cocktail_text.append(f"Garnish: {cocktail.garnish}")
    else:
        cocktail_text.append("Garnish: not specified")

    cocktail_text.append("")

    cocktail_text.append("Ingredients:")
    for ingredient in cocktail.ingredients:
        line = format_ingredient(ingredient)
        
        cocktail_text.append(line)
    
    if cocktail.source_url:
        cocktail_text.append("")
        cocktail_text.append("Source:")
        cocktail_text.append(cocktail.source_url)
    text = "\n".join(cocktail_text)

    return text