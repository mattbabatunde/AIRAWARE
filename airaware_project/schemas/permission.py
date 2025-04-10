from pydantic import BaseModel, EmailStr, constr, Field
from datetime import datetime
from typing import Optional, Union



class RoleCreate(BaseModel):
    role_name: str

class Role(RoleCreate):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  


    class Config:
        orm_mode = True

class UserRoleCreate(BaseModel):
    user_id: str
    role_id: str

class UserRoleResponse(UserRoleCreate):
    id: str

    class Config:
        orm_mode = True

class PermissionCreate(BaseModel):
    permission_name: str

class PermissionResponse(PermissionCreate):
    id: str

    class Config:
        orm_mode = True

class RolePermissionCreate(BaseModel):
    role_id: str
    permission_id: str

class RolePermissionResponse(RolePermissionCreate):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  
    

    class Config:
        orm_mode = True