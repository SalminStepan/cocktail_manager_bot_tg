# Этот файл описывает Pydantic-схемы ингредиентов.
# Он отделяет формат входных ингредиентов от формата строк, которые читаются из импортированной ETL-базы.

from pydantic import BaseModel
from decimal import Decimal

# Описывает ингредиент, который вводится вручную через FSM.
class IngredientCreate(BaseModel):
    name: str
    amount: int
    unit: str
    comment: str | None = None

# Описывает ингредиент, прочитанный из нормализованной базы.
class IngredientRead(BaseModel):
    id: int
    position: int
    raw: str
    amount: Decimal | None
    unit: str | None
    name: str | None
    comment: str | None
    unresolved: bool
