from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    text: str = Field(max_length=150)
    timestamp: datetime
    status: bool = False


class TaskCreate(BaseModel):
    pass