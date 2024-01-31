from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("")
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{user_id}")
async def get_specific_user(user_id: int):
    return {"user_id": user_id}


@router.post("/create")
async def create_user():
    pass