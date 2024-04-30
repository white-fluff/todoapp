import uuid
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ShowTask(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: int
    text: str
    timestamp: datetime
    status: bool = False


class CreateTask(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: uuid.UUID
    text: str = Field(max_length=150)
    status: bool = False
