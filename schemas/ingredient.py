from pydantic import BaseModel
from decimal import Decimal

class IngredientCreate(BaseModel):
    name: str
    amount: int
    unit: str
    comment: str | None = None

class IngredientRead(BaseModel):
    id: int
    position: int
    raw: str
    amount: Decimal | None
    unit: str | None
    name: str | None
    comment: str | None
    unresolved: bool