import re
import uuid
from fastapi import HTTPException
from pydantic import BaseModel, ConfigDict
from pydantic import EmailStr, Field
from pydantic import field_validator


USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_@+\-=*&%.{}[\]()]+$")


class ShowUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr
    username: str
    registered_at: str
    is_active: bool


class CreateUser(BaseModel):
    username: str = Field(max_length=15)
    email: EmailStr
    password: str = Field(max_length=100)

    @classmethod
    @field_validator("username")
    def validate_username(cls, value):
        if not USERNAME_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letters"
            )
        return value
