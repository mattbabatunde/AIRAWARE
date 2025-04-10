from pydantic import BaseModel, EmailStr, constr, Field
from datetime import datetime
from typing import Optional, Union

class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
   


class UserDb(UserBase):
    id: str
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
  

class UserCreate(UserBase):
    password: str


class User(UserBase):
    pass


class UserUpdate(UserBase):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    pass

class UserPasswordUpdate(BaseModel):
    current_password: str
    new_password: str





