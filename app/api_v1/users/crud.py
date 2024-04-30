from .schemas import ShowUser, CreateUser


def get_user(user_id: int) -> dict:
    # user = user_id.model_dump()
    user = "fakeUserName"
    return {
        "user": user
    }


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()
    return {
        "status": 200,
        "success": True,
        "user": user
    }


def update_user(user_id: int) -> dict:
    user = user_id.model_dump()
    return {
        "status": 200,
        "success": True,
        "user": user
    }


def delete_user(user_id: int) -> dict:
    user = "fakeUserName"
    return {
        "status": 200,
        "success": True,
        "user": user
    }
