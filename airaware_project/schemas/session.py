from pydantic import BaseModel, constr, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime


class UserSessionCreate(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user")
    session_token: str = Field(..., description="Token for this session")
    ip_address: Optional[str] = Field(None, max_length=45, description="IPv4 or IPv6 address")
    user_agent: Optional[str] = Field(None, description="User agent string")
    created_at: datetime = Field(..., description="Session creation time")
    expires_at: datetime = Field(..., description="Session expiration time")

class UserSession(UserSessionCreate):
    id: str

    model_config = {
        "from_attributes": True
    }













