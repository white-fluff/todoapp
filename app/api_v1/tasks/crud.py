from sqlalchemy import select, insert, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Task, TaskCreate
from app.db.models import tasks


async def get_task(task_id: int, session: AsyncSession) -> Task | None:
    stmt = select(tasks).where(tasks.c.id == task_id)
    task = await session.execute(stmt)

    task_tuple = task.all()[0]

    return Task(
        id=task_tuple[0],
        user_id=task_tuple[1],
        text=task_tuple[2],
        timestamp=task_tuple[3],
        status=task_tuple[4]
    )


async def create_task(new_task: TaskCreate, session: AsyncSession) -> dict | None:
    stmt = insert(tasks).values(**new_task.dict())  # bad temporary solution
    await session.execute(stmt)
    await session.commit()

    return new_task.dict()


async def update_task(task_id: int) -> dict:
    pass


async def delete_task(task_id: int, session: AsyncSession) -> dict:
    try:
        stmt = delete(tasks).where(tasks.c.id == task_id)
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

