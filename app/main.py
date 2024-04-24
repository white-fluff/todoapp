# import uvicorn
from fastapi import FastAPI
from api_v1 import router


app = FastAPI(
    title="Yet Another ToDo App"
)

app.include_router(router)


# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
