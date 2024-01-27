from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    id: int
    user_id: int
    text: str
    timestamp: datetime
    status: bool = False
