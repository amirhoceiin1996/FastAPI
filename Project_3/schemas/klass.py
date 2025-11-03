from pydantic import BaseModel


class ClassSchema(BaseModel):
    id: int
    name: str
    teacher_name: str
    
    class Config:
        from_attributes = True


class ClassCreateSerializer(BaseModel):
    name: str
    teacher_name: str