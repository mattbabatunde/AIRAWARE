
from pydantic import BaseModel, constr, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime



class AQIRecordCreate(BaseModel):
    location_id: str
    recorded_at: datetime
    aqi_score: float
    health_implication: Optional[str]

class AQIRecord(AQIRecordCreate):
    id: str 
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  
    class Config:
        orm_mode = True

class AQIForecastCreate(BaseModel):
    location_id: str
    predicted_at: datetime
    forecast_source: Optional[str]
    aqi_score: float
    health_implication: Optional[str]

class AQIForecast(AQIForecastCreate):
    id: str

    class Config:
        orm_mode = True