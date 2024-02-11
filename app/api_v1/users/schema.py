from pydantic import BaseModel, EmailStr


class User(BaseModel):
    # ToDo: registered_at
    id: int
    email: EmailStr
    username: str
    password: str
    is_active: bool = True
    is_superuser: bool = False


class CreateUser(BaseModel):
    username: str
    email: EmailStr
