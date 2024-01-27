from fastapi import FastAPI
from app.api.users.router import router as router_users
from app.api.tasks.router import router as router_tasks

app = FastAPI(
    title="Yet Another ToDo App"
)

app.include_router(router_users)
app.include_router(router_tasks)
