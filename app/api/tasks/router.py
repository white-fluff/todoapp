from fastapi import APIRouter
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.tasks.schemas import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("")
async def get_specific_task():
    return [{"task0": "TaskTest"}, {"task1": "TaskTest"}]

@router.post("")
async def create_task():
    pass

@router.post("")
async def change_task():
    pass

@router.delete("")
async def delete_task():
    pass

