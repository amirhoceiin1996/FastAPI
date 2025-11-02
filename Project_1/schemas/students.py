from pydantic import BaseModel, Field, conint, ConfigDict
from typing import Annotated, Optional, Any
from datetime import datetime


class UserIn(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    age: conint(gt=0)
    grade: Annotated[str, Field(min_length=1)]

class UserOut(BaseModel):
    name: str
    age: int
    grade: str
    is_active: bool = True
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class Status_check(BaseModel):
    status: str
    message: str
    data: Optional[Any] = None
