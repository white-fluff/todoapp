from typing import List, Annotated

from fastapi import APIRouter, Depends, Path, Body, HTTPException, status
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
async def get_specific_task(
        task_id: Annotated[int, Path(ge=1, lt=1_000_001)],
        session: AsyncSession = Depends(get_async_session)
):
    task = await crud.get_task(task_id, session)

    if task is not None:
        return {
            "status": "success",
            "task": task
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Task {task_id} not found!'
    )


@router.post("")
async def create_task(
        task: TaskCreate,
        session: AsyncSession = Depends(get_async_session)
):

    task = await crud.create_task(new_task=task, session=session)

    if task is not None:
        return {
            "status": "success",
            "task": task
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Internal Server Error\nFailed creation task operation.'
    )


# @router.put("")
# async def update_task():
#     return {
#         "status": "success",
#         "task": "task"
#     }


# Delete task (DELETE)
@router.delete("/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    return await crud.delete_task(task_id=task_id, session=session)
