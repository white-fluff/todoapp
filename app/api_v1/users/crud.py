import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from asyncpg.exceptions import UniqueViolationError

from app.hashing import HashPass
from .schemas import ShowUser, CreateUser
from app.db.models import User


async def create_user(body: CreateUser, session: AsyncSession) -> ShowUser | None:
    async with session.begin():
        new_user = User(
            email=body.email,
            username=body.username,
            password=HashPass.hash_password(body.password)
        )

        session.add(new_user)
        try:
            await session.flush()
        except UniqueViolationError:
            return None

    return ShowUser(
        id=new_user.id,
        email=new_user.email,
        username=new_user.username,
        registered_at=new_user.registered_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        is_active=new_user.is_active
    )


async def get_user_by_username(username: str, session: AsyncSession) -> ShowUser | None:
    async with session.begin():
        stmt = select(User).where(User.username == username)
        resp_user = await session.execute(stmt)
        user_row = resp_user.fetchone()

        if user_row is None:
            return None
        else:
            return ShowUser(
                id=user_row[0].id,
                email=user_row[0].email,
                username=user_row[0].username,
                registered_at=user_row[0].registered_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
                is_active=user_row[0].is_active
            )


async def get_user_by_id(user_id: str, session: AsyncSession) -> ShowUser | None:
    uuid_id = uuid.UUID(user_id)
    async with session.begin():
        stmt = select(User).where(User.id == uuid_id)
        resp_user = await session.execute(stmt)
        user_row = resp_user.fetchone()

        if user_row is None:
            return None
        else:
            return ShowUser(
                id=user_row[0].id,
                email=user_row[0].email,
                username=user_row[0].username,
                registered_at=user_row[0].registered_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
                is_active=user_row[0].is_active
            )


async def update_user(user_id: int) -> ShowUser:
    pass


async def delete_user(user_id: int) -> ShowUser:
    pass
