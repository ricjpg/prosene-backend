from pydantic import EmailStr, BaseModel
from typing import Optional, Union


class EstadoSolicitudCreate(BaseModel):
    idestadosolicitud: int
    descripcion: str
    class Config:
        orm_mode = True
    

class EstadoSolicitudOutput(BaseModel):
    idestadosolicitud: Optional[int]
    descripcion: Optional[str]
    class Config:
        orm_mode = True