from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.hashing import HashPass
from .schemas import ShowUser, CreateUser
from app.db.models import User


def get_user(user_id: int) -> dict:
    user = "fakeUserName"
    return {
        "user": user
    }


async def create_user(body: CreateUser, session: AsyncSession) -> ShowUser:
    # user = user_in.model_dump()
    async with session.begin():
        new_user = User(
            email=body.email,
            username=body.username,
            password=HashPass.hash_password(body.password)
        )

        session.add(new_user)
        await session.flush()

    return ShowUser(
        id=new_user.id,
        email=new_user.email,
        username=new_user.username,
        registered_at=new_user.registered_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        is_active=new_user.is_active
    )


def update_user(user_id: int) -> dict:
    user = user_id.model_dump()
    return {
        "status": 200,
        "success": True,
        "user": user
    }


def delete_user(user_id: int) -> dict:
    user = "fakeUserName"
    return {
        "status": 200,
        "success": True,
        "user": user
    }
