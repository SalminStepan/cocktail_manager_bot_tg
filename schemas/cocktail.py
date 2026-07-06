from datetime import datetime
from pydantic import BaseModel
from schemas.ingredient import IngredientCreate, IngredientRead


class CocktailCreate(BaseModel):
    name: str
    glass: str
    garnish: str
    method: str
    ingredients: list[IngredientCreate]

class CocktailRead(BaseModel):
    id: int
    name: str
    description: str | None
    image_url: str | None
    glass: str | None
    garnish: str | None
    method: str | None
    parse_status: str
    source_url: str | None
    ingredients: list[IngredientRead]
    created_at: datetime | None