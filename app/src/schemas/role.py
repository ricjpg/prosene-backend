from pydantic import EmailStr, BaseModel
from typing import Optional, Union


class RolInCreate(BaseModel):
    idcentroregional: int
    centroregional: str
    class Config:
        orm_mode = True
    

class RolOutput(BaseModel):
    idcentroregional: int
    centroregional: str
    class Config:
        orm_mode = True