from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import ShowUser, CreateUser
from app.db.database import get_async_session


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", response_model=ShowUser)
async def create_user(user: CreateUser,  session: AsyncSession = Depends(get_async_session)) -> ShowUser:
    return await crud.create_user(body=user, session=session)


@router.get("/{user_id}", response_model=ShowUser)
async def get_user(user_id: int):
    return 


@router.patch("/{user_id}/update")
async def update_user(user_id: int):
    pass


@router.delete("/{user_id}/delete")
async def delete_user(user_id: int):
    pass
