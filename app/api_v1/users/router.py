from fastapi import APIRouter

from . import crud
from .schema import User, CreateUser


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/create")
async def create_user(user: CreateUser):
    return crud.create_user(user_in=user)


@router.get("/{user_id}")
async def get_user(user_id: int):
    return 


@router.patch("/{user_id}/update")
async def update_user(user_id: int):
    pass


@router.delete("/{user_id}/delete")
async def delete_user(user_id: int):
    pass
