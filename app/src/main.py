from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from .utils.init_db import create_tables
from .api.v1.routers import router
from .utils.protectRoute import get_current_user
from .schemas.user import UserOutput
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize db
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
origins = [
    "http://localhost:3000",  # React/Vite corriendo en este puerto
    "http://localhost:5173",  # Vite por defecto
    "http://localhost:4200",  # Angular por defecto
    "http://localhost:8000",  # FastAPI mismo (si usas en frontend separado)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Include OPTIONS
    allow_headers=["*"],  # Allow all headers
)
app.include_router(router)
