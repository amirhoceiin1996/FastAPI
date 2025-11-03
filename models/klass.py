from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.student import Student


class Klass(SQLModel, table=True):
    __tablename__ = "classes"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    teacher_name: str
    
    students: list["Student"] = Relationship(back_populates="klass")