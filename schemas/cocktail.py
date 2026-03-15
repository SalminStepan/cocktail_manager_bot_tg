from datetime import datetime
from pydantic import BaseModel
from ingredient import IngredientCreate, IngredientRead

class CocktailCreate(BaseModel):
    name: str
    glass: str
    garnish: str
    method: str
    ingredients: list[IngredientCreate]

class CocktailRead(BaseModel):
    id: int
    name: str
    glass: str
    garnish: str
    method: str
    ingredients: list[IngredientRead]
    created_at: datetime