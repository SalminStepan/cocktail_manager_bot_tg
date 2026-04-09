from pydantic import BaseModel

class IngredientCreate(BaseModel):
    name: str
    amount: int
    unit: str
    comment: str | None = None

class IngredientRead(BaseModel):
    id: int
    name: str
    amount: int
    unit: str
    comment: str | None = None
