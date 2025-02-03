from fastapi import APIRouter
from .endpoints import auth, users

router = APIRouter(prefix="/api/v1")
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(auth.router, prefix="/auth", tags=["auth"])