from pydantic import BaseModel, EmailStr, constr, Field
from datetime import datetime
from typing import Optional, Union



class HealthTipBase(BaseModel):
    health_tip_context: str
    sent_at: datetime

class HealthTipCreate(HealthTipBase):
    user_id: str

class HealthTipResponse(HealthTipBase):
    id: int
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  

    class Config:
        orm_mode = True
