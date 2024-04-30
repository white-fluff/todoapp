import uuid

from fastapi import APIRouter, Depends, Path, Body, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import ShowTask, CreateTask
from app.db.database import get_async_session


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("")
async def get_tasks():
    pass


@router.get("/{task_id}", response_model=ShowTask)
async def get_task_by_id(
        task_id: uuid.UUID,
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


@router.post("", response_model=ShowTask)
async def create_task(
        body: CreateTask,
        session: AsyncSession = Depends(get_async_session)
):

    task = await crud.create_task(new_task=body, session=session)

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
