from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Union
from decimal import Decimal

class ProductBase(BaseModel):
    product_url: str
    product_description: str
    product_name: str
    product_price: Decimal



class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  
    

    class Config:
        orm_mode = True

