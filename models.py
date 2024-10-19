from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    @classmethod
    def validate(cls, v, *, strict=False, from_attributes=False, context=None):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return str(v)


class Task(BaseModel):
    id: Optional[PyObjectId] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}