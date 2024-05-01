import uuid

from sqlalchemy import select, insert, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ShowTask, CreateTask
from app.db.models import Task


async def get_task(task_id: uuid.UUID, session: AsyncSession) -> ShowTask:
    stmt = select(task).where(task.c.id == task_id)
    specific_task = await session.execute(stmt)

    task_tuple = specific_task.all()[0]

    return ShowTask(
        id=task_tuple[0],
        user_id=task_tuple[1],
        text=task_tuple[2],
        timestamp=task_tuple[3],
        status=task_tuple[4]
    )


async def create_task(new_task: CreateTask, session: AsyncSession) -> ShowTask:
    pass
    # stmt = insert(task).values(**new_task.dict())
    # await session.execute(stmt)
    # await session.commit()
    #
    #
    # return ShowTask(
    #     # id=
    #     # user_id=
    #     # text=
    #     # timestamp=
    #     # status=
    # )


async def update_task(task_id: int) -> dict:
    pass


async def delete_task(task_id: int, session: AsyncSession) -> dict:
    try:
        stmt = delete(task).where(task.c.id == task_id)
        result = await session.execute(stmt)
        num_deleted = result.rowcount
        await session.commit()

        if num_deleted == 1:
            return {
                "status": "success",
                "description": f"Task {task_id} was successful deleted."
            }
        elif num_deleted == 0:
            return {
                "status": "success",
                "description": f"Task with id {task_id} doesn't exist."
            }
    except SQLAlchemyError as err:
        await session.rollback()
        print(f"LOG:{err}")
        return {
            "status": "Internal Server Error",
            "description": f"Failed deleting task operation."
        }

