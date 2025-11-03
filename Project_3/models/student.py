from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

if TYPE_CHECKING:
    from models.klass import Klass
    from models.parent import Parent


class Student(SQLModel, table=True):
    __tablename__ = "students"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    grade: str
    class_id: int = Field(foreign_key="classes.id")
    parent_id: int = Field(foreign_key="parents.id")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    klass: Optional["Klass"] = Relationship(back_populates="students")
    parent: Optional["Parent"] = Relationship(back_populates="students")