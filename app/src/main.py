from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from .utils.init_db import create_tables
from .api.v1.routers import router
from .utils.protectRoute import get_current_user
from .schemas.user import UserOutput

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize db
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)