from pydantic import EmailStr, BaseModel
from typing import Optional, Union


class TipoSolicitudCreate(BaseModel):
    idtiposolicitud: int
    descripcion: str
    class Config:
        orm_mode = True
    

class TipoSolicitudOutput(BaseModel):
    idtiposolicitud: int
    descripcion: str

    class Config:
        orm_mode = True
    