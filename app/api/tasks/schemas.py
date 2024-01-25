from pydantic import BaseModel
from typing import List
from datetime import datetime

class TaskCreate(BaseModel):
    id: int
    user_id: int
    text: str
    timestamp: datetime
    status: bool = False
