
from pydantic import BaseModel, constr, Field
from typing import Optional, Union
from enum import Enum
from datetime import datetime



class Gender(str, Enum):
    male = "male"
    female = "female"



class UserType(str, Enum):
    caring_parent = "caring_parent"
    researcher = "researcher"
    outdoor_worker = "outdoor_worker"
    environmental_enthusiast = "environmental_enthusiast"
    other = "other"




class ProfileBase(BaseModel):
    user_type: Optional[UserType] 
    image_url: Optional[str] 
    gender: Optional[Gender]
    user_interest: Optional[str]
    bio: Optional[str]
    health_condition: Optional[str]
    location: Optional[str]
    age: int
    timezone: Optional[str]
    


class ProfileCreate(ProfileBase):
    user_id: str
  


class UserProfileResponse(ProfileBase):
    id: str
    created_at: Union[datetime, str] = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")  






