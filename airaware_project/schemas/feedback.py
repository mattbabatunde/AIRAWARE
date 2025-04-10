from pydantic import BaseModel, constr, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime




class FeedbackCreate(BaseModel):
    user_id: str
    feedback_text: str


class FeedbackResponse(FeedbackCreate):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  

    class Config:
        orm_mode = True