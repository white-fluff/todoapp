from fastapi import APIRouter
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.tasks.schemas import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Read task (GET)
@router.get("")
async def get_task():
    return [{"task0": "TaskTest"}, {"task1": "TaskTest"}]

# Create task (POST, PUT if we have `id` or `uuid`)
@router.post("")
async def create_task():
    pass

# Update task (PUT to replace, PATCH to modify )
@router.put("")
async def update_task():
    pass

# Deleta task (DELETE)
@router.delete("")
async def delete_task():
    pass

