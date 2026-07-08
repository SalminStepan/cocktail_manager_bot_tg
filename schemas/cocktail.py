# Этот файл описывает Pydantic-схемы коктейля для создания и чтения.
# Он нужен как общий контракт между handlers, services и repositories, чтобы данные имели предсказуемую структуру.

from datetime import datetime
from pydantic import BaseModel
from schemas.ingredient import IngredientCreate, IngredientRead


# Описывает входные данные для создания коктейля вручную.
class CocktailCreate(BaseModel):
    name: str
    glass: str
    garnish: str
    method: str
    ingredients: list[IngredientCreate]

# Описывает полную карточку коктейля, которую читает бот.
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
