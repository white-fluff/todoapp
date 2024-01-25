from fastapi import FastAPI
from app.api.users import users
from app.api.tasks import router as router_tasks

app = FastAPI(
    title="Yet Another ToDo App"
)

app.include_router(users.router)
app.include_router(router_tasks.router)
