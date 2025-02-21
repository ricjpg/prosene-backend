from fastapi import APIRouter
from .endpoints import auth, users, formulario, solicitudes, misc

router = APIRouter(prefix="/api/v1")
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(formulario.router, prefix="/form", tags=["form"])
router.include_router(solicitudes.router, prefix="/solicitudes", tags=["solicitudes"])
router.include_router(misc.router, prefix="/varios", tags=["varios"])