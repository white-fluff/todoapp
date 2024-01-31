import uvicorn
from fastapi import FastAPI
from api.users.router import router as router_users
from api.tasks.router import router as router_tasks


app = FastAPI(
    title="Yet Another ToDo App"
)

app.include_router(router_users)
app.include_router(router_tasks)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)