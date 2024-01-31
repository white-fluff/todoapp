from datetime import datetime
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    user_id: int
    text: str = Field(max_length=150)
    timestamp: datetime
    status: bool = False
