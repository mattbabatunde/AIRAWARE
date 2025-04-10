from pydantic import BaseModel, constr, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime



class PollutantCreate(BaseModel):
    pollutant_name: str
    location_id: str
    pollutant_level: int
    pollutant_score: float
    recorded_at: datetime

class Pollutant(PollutantCreate):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  

    class Config:
        orm_mode = True

class AQIPollutantCreate(BaseModel):
    pollutant_id: str
    aqi_id: str

class AQIPollutantResponse(AQIPollutantCreate):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  

    class Config:
        orm_mode = True

    
