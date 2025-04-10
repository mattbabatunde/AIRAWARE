from pydantic import BaseModel, EmailStr, constr, Field
from datetime import datetime
from typing import Optional, Union




class ActivityLogCreate(BaseModel):
    user_id: str
    activity_type: str
    description: Optional[str]


class ActivityLog(ActivityLogCreate):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  
    

    class Config:
        orm_mode = True