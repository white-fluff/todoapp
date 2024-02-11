from fastapi import APIRouter
from .users.router import router as router_users
from .tasks.router import router as router_tasks


router = APIRouter()

router.include_router(router_users)
router.include_router(router_tasks)
