from pydantic import BaseModel


class ClassCreateSerializer(BaseModel):
    name: str
    teacher_name: str


class ClassResponseSerializer(BaseModel):
    id: int
    name: str
    teacher_name: str
    
    class Config:
        from_attributes = True