from pydantic import BaseModel, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime

class NotificationType(str, Enum):
    location_based = "location_based"
    severe_warnings = "severe_warnings"
    realtime_updates = "realtime_updates"
    aqi_forecasts = "aqi_forecasts"

class NotificationBase(BaseModel):
    notification_context: str
    notification_type: Optional[NotificationType]
    sent_at: datetime

class NotificationCreate(NotificationBase):
    user_id: str

class Notification(NotificationBase):
    id: int
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  

