from pydantic import EmailStr, BaseModel
from typing import Optional, Union


class RolesCreate(BaseModel):
    idrol: int
    descripcion: str
    class Config:
        orm_mode = True
    

class RolesOutput(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True