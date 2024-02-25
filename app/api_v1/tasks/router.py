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
) -> List[tuple]:
    stmt = select(tasks).where(tasks.c.id == task_id)
    result = await session.execute(stmt)
    task = result.all()
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


@router.post("")
async def create_task(task: TaskCreate):
    return crud.create_task(task_in=task)


# @router.put("")
# async def update_task():
#     pass

# # Delete task (DELETE)
# @router.delete("")
# async def delete_task(task_id):
#     pass
