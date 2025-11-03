from pydantic import BaseModel, field_validator
from datetime import datetime
from schemas.parent import ParentSchema
from schemas.klass import ClassSchema


class StudentCreateSchema(BaseModel):
    name: str
    age: int
    grade: str
    class_id: int
    parent_id: int
    
    @field_validator('age')
    @classmethod
    def validate_age(cls, v):
        if v < 6:
            raise ValueError('Student too young for registration')
        return v


class StudentResponseSchema(BaseModel):
    id: int
    name: str
    grade: str
    is_active: bool
    created_at: datetime
    class_info: ClassSchema
    parent: ParentSchema
    
    class Config:
        from_attributes = True