from pydantic import BaseModel, EmailStr, constr, Field
from datetime import datetime
from typing import Optional, Union



class CartCreate(BaseModel):
    user_id: str

class Cart(CartCreate):
    id: str


class CartItemCreate(BaseModel):
    cart_id: int
    product_id: int
    quantity: int

class CartItemResponse(CartItemCreate):
    id: int

    model_config = {
        "from_attributes": True
    }