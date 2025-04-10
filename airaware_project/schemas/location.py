
from pydantic import BaseModel, constr, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime


class LocationBase(BaseModel):
    location_name: str
    area: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: str

    class Config:
        orm_mode = True

class WhitelistedLocationCreate(BaseModel):
    user_id: str
    location_id: str

class WhitelistedLocationResponse(WhitelistedLocationCreate):
    id: str
