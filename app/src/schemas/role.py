from pydantic import EmailStr, BaseModel
from typing import Union


class RolInCreate(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True
    