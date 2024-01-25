from pydantic import BaseModel

class User(BaseModel):
    # ToDo: registered_at
    id: int
    email: str
    username: str
    password: str
    is_active: bool = True
    is_superuser: bool = False
