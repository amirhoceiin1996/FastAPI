from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.klass import Klass


class Student(SQLModel, table=True):
    __tablename__ = "students"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    grade: str
    class_id: int = Field(foreign_key="classes.id")
    
    klass: Optional["Klass"] = Relationship(back_populates="students")