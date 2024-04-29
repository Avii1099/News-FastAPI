from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str


class ItemCreate(ItemBase):
    data: str


class Item(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True
