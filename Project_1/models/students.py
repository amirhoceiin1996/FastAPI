from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    age: int = Field(nullable=False)
    grade: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(), nullable=False)