from pydantic import EmailStr, BaseModel
from typing import Optional, Union


class NacionalidadCreate(BaseModel):
    idnacionalidad: int
    nacionalidad: str
    class Config:
        orm_mode = True
    

class NacionalidadOutput(BaseModel):
    idnacinoalidad: Optional[int]
    nacionalidad: Optional[str]
    class Config:
        orm_mode = True