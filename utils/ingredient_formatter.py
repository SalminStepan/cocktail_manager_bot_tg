# Этот файл форматирует ингредиент для вывода в карточке коктейля.
# Он учитывает нормализованные и unresolved-ингредиенты, чтобы пользователь всегда видел читаемую строку.

from schemas.ingredient import IngredientRead

# Преобразует IngredientRead в одну строку для карточки рецепта.
def format_ingredient(ingredient: IngredientRead) -> str:
    ingredient_form =["-"]

    if ingredient.unresolved:
        ingredient_form.append(ingredient.raw)
        return " ".join(ingredient_form)

    if ingredient.amount is not None:
        ingredient_form.append(f"{ingredient.amount} {ingredient.unit} {ingredient.name}")
        if ingredient.comment:
            ingredient_form.append(f"({ingredient.comment})")
        return " ".join(ingredient_form)
    
    if not ingredient.amount is None and ingredient.unit and ingredient.name:
        ingredient_form.append(f"{ingredient.unit} {ingredient.name}")
        if ingredient.comment:
            ingredient_form.append(f"({ingredient.comment})")
        return " ".join(ingredient_form)
    
    return f"- {ingredient.raw}"
