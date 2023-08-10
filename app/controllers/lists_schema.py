from pydantic import BaseModel


class ListBase(BaseModel):
    name: str
    description: str
    items: dict


class ListCreate(ListBase):
    pass

class List(ListBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True