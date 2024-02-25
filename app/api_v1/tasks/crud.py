
# from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Task, TaskCreate


async def get_task(task_id: int, session: AsyncSession) -> Task | None:
    # return await session.get(Task, task_id)
    pass


def create_task(task_in: TaskCreate) -> dict:
    task = task_in.model_dump()
    return {
        "status": 200,
        "success": True,
        "task": task
    }


def update_task(task_id: int) -> dict:
    task = "fakeTask"
    return {
        "status": 200,
        "success": True,
        "task": task
    }


def delete_task(task_id: int) -> dict:
    task = "fakeTask"
    return {
        "status": 200,
        "success": True,
        "task": task
    }
