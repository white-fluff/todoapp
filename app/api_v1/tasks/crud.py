from .schemas import Task, TaskCreate


def get_task(task_id: int) -> dict:
    # task = task_id.model_dump()
    task = "fakeTask"
    return {
        "task": task
    }


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