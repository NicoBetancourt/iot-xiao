from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    item: str
    quantity: int


class ProductList(BaseModel):
    _id: Optional[str]
    date: str
    products: list[Product]
