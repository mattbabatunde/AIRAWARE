
from pydantic import BaseModel, constr, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime




class SoldProductCreate(BaseModel):
    user_id: str
    product_id: str
    sold_at: datetime

class Response(SoldProductCreate):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  
