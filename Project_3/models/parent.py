from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.student import Student


class Parent(SQLModel, table=True):
    __tablename__ = "parents"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    phone_number: str
    
    students: list["Student"] = Relationship(back_populates="parent")