from typing import List

from fastapi import APIRouter, Depends, Body, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Task, TaskCreate
from app.db.database import get_async_session
from app.db.models import tasks


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("")
async def get_tasks():
    pass


@router.get("/{task_id}")
async def get_specific_task(task_id: int, session: AsyncSession = Depends(get_async_session)) -> List[tuple]:
    stmt = select(tasks).where(tasks.c.id == task_id)
    result = await session.execute(stmt)
    task = result.all()
    print(task)
    print(type(task))
    return task

    # task = await crud.get_task(task_id, session)
    #
    # if task is not None:
    #     return task
    #

    # raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND,
    #     detail=f'Task {task_id} not found!'
    # )

# @router.post("")
# async def create_task(task: List[Task]):
#     fake_tasks.extend(task)
#     return {"status": 200, "data": fake_tasks}    


# @router.put("")
# async def update_task():
#     pass

# # Delete task (DELETE)
# @router.delete("")
# async def delete_task(task_id):
#     pass
