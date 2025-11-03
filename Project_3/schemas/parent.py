from pydantic import BaseModel


class ParentSchema(BaseModel):
    id: int
    name: str
    phone_number: str
    
    class Config:
        from_attributes = True


class ParentCreateSerializer(BaseModel):
    name: str
    phone_number: str