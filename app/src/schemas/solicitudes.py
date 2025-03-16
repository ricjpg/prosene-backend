from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
from .estadoSolicitud import EstadoSolicitudOutput
from .tipoSolicitud import TipoSolicitudOutput
from .user import UserOutput



class SolicitudesCreate(BaseModel):
    idusuariosolicitante: Optional[int]
    idresponsablesolicitud: Optional[int] = 1
    idtiposolicitud: int
    idestadosolicitud: Optional[int] = 1
    fechacreacion: Optional[datetime] = datetime.today()
    descripcion: Optional[str]
    class Config:
        orm_mode = True
    

class SolicitudesOutput(BaseModel):
    idsolicitud: Optional[int] = None
    idusuariosolicitante: Optional[int] = None
    idresponsablesolicitud: Optional[int] = None
    usuariosolicitante: Optional[UserOutput] = None
    responsablesolicitud: Optional[UserOutput] = None
    estadosolicitud: Optional[EstadoSolicitudOutput] = None
    tiposolicitud: Optional[TipoSolicitudOutput] = None
    fechacreacion: Optional[datetime] = None
    descripcion: Optional[str] = None
    class Config:
        orm_mode = True


class SolicitudUpdate(BaseModel):
    idsolicitud: Optional[int] = None
    idresponsablesolicitud: Optional[int] = None
    idestadosolicitud: Optional[int] = None

class SolicitudEditar(BaseModel):
    idsolicitud: Optional[int] = None
    idtiposolicitud: Optional[int] = None
    fechacreacion: Optional[datetime] = None
    descripcion: Optional[str] = None
    class Config:
        orm_mode = True

class AsignarSchema(BaseModel):
    idsolicitud: Optional[int]
    idresponsablesolicitud: Optional[int]