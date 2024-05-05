from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import ShowUser, CreateUser
from app.db.database import get_async_session


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", response_model=ShowUser)
async def create_user(user: CreateUser,  session: AsyncSession = Depends(get_async_session)):
    user = await crud.create_user(body=user, session=session)
    if user is None:
        raise HTTPException(
            status_code=400,
            detail=f"Some shit happened. I just don't know how to process it yet. But he's definitely wrong :)"
        )
    return user


@router.get("/{username}", response_model=ShowUser)
async def get_user_by_username(username: str, session: AsyncSession = Depends(get_async_session)):
    user = await crud.get_user_by_username(username=username, session=session)
    if user is None:
        raise HTTPException(
            status_code=404, detail=f"User with name {username} not found."
        )
    return user


@router.get("/id/{user_id}", response_model=ShowUser)
async def get_user_by_id(user_id: str,  session: AsyncSession = Depends(get_async_session)) -> ShowUser:
    user = await crud.get_user_by_id(user_id=user_id, session=session)
    if user is None:
        raise HTTPException(
            status_code=404, detail=f"User with id {user_id} not found."
        )
    return user


# ToDo: change it:

# @router.patch("/{user_id}/update")
# async def update_user(user_id: str, response_model=ShowUser):
#     pass
#
#
# @router.delete("/{user_id}/delete")
# async def delete_user(user_id: int, response_model=ShowUser):
#     pass
