from fastapi import APIRouter

from . import crud
from .schemas import Task, TaskCreate


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("")
async def get_tasks():
    pass


@router.get("/{task_id}")
async def get_specific_task(task_id: int): 
    pass


# @router.post("")
# async def create_task(task: List[Task]):
#     fake_tasks.extend(task)
#     return {"status": 200, "data": fake_tasks}    


# @router.put("")
# async def update_task():
#     pass

# # Deleta task (DELETE)
# @router.delete("")
# async def delete_task(task_id):
#     pass
