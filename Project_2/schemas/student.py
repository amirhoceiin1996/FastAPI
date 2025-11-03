# schemas/student.py
from pydantic import BaseModel


class StudentCreateSerializer(BaseModel):
    name: str
    age: int
    grade: str
    class_id: int


class ClassSerializer(BaseModel):
    id: int
    name: str
    teacher_name: str
    
    class Config:
        from_attributes = True


class StudentResponseSerializer(BaseModel):
    id: int
    name: str
    grade: str
    class_info: ClassSerializer
    
    class Config:
        from_attributes = True