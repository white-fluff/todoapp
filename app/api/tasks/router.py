# from typing import List
from fastapi import APIRouter
# from api.tasks.schemas import Task


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("")
async def get_tasks():
    return [{"status": 200, "data": fake_tasks}]


@router.get("/{task_id}")
async def get_specific_task(task_id: int): 
    for task in fake_tasks:
        if task.get("id") == task_id:
            return [{"status": 200, "data": task}]
    return [{"status": 204, "data": "No Content"}]


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
