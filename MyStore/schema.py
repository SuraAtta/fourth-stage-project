from ninja import Schema
from pydantic import EmailStr, Field
from typing import List


class FourOFourOut(Schema):
    detail: str

class CategorySchema(Schema):
    name : str
  

class ColorSchema(Schema):
    color_code: str


class ColorIn(Schema):
    title: str
    color_code: str


class ProductImageSchema(Schema):
    image: str
  
class ProductSchema(Schema):
    id: int
    title: str
    banner: str
    description: str = None
    category: CategorySchema
    colors: List[ColorSchema]
    price: int
    stock: int
    is_available: bool = True
    show_hide: bool = True
    is_fav: bool = False
    product_image: List[ProductImageSchema]

class ItemSchema(Schema):
    product: ProductSchema
    quantity: int
    is_ordered: bool

class ItemCreate(Schema):
    product_id: int
    quantity: int = 1


class ItemOut(ItemSchema):
    id: int