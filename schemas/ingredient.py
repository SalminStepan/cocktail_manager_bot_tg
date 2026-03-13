from pydantic import BaseModel

class IngredientCreate(BaseModel):
    name: str
    amount_ml: int

class IngredientRead(BaseModel):
    id: int
    name: str
    amount_ml: int
