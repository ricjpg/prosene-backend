from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
from sqlalchemy import TIMESTAMP
from .estadoSolicitud import EstadoSolicitudOutput
from .tipoSolicitud import TipoSolicitudOutput
from .user import UserOutput



class SolicitudesCreate(BaseModel):
    idusuariosolicitante: Optional[int]
    idresponsablesolicitud: Optional[int] = 1
    idtiposolicitud: int
    idestadosolicitud: Optional[int] = 1
    fechacreacion: Optional[datetime]
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
    toBecario: Optional[bool]
    nombreBecario: Optional[str]
    retroalimentacionEnProceso: Optional[str] 
    retroalimentacionFinalizada: Optional[str] 
    retroalimentacionCancelada: Optional[str] 
    retroalimentacionRecibida: Optional[str] 
    retroalimentacionRechazada: Optional[str] 
    class Config:
        orm_mode = True


class SolicitudUpdate(BaseModel):
    idsolicitud: Optional[int] = None
    idresponsablesolicitud: Optional[int] = None
    idestadosolicitud: Optional[int] = 2
    retroalimentacionRecibida: Optional[str] = None
    retroalimentacionEnProceso: Optional[str] = None
    retroalimentacionFinalizada: Optional[str] = None
    retroalimentacionCancelada: Optional[str] = None
    retroalimentacionRechazada: Optional[str] = None

class SolicitudEditar(BaseModel):
    idsolicitud: Optional[int] = None
    idtiposolicitud: Optional[int] = None
    fechacreacion: Optional[datetime] = None
    descripcion: Optional[str] = None
    class Config:
        orm_mode = True

class AsignarColaborador(BaseModel):
    idsolicitud: Optional[int]
    idresponsablesolicitud: Optional[int]
    idestadosolicitud: Optional[int] = 2
    retroalimentacionEnProceso: Optional[str] = "No hay retroalimentacion"

class AsignarBecario(BaseModel):
    idsolicitud: Optional[int]
    idresponsablesolicitud: Optional[int]
    idestadosolicitud: Optional[int] = 2
    toBecario: Optional[bool] = True
    nombreBecario: str
    retroalimentacionEnProceso: Optional[str] = "No hay retroalimentacion"

class AtenderSolicitud(BaseModel):
    idsolicitud: Optional[int]
    idresponsablesolicitud: Optional[int]
    idestadosolicitud: Optional[int] = 2
    retroalimentacionEnProceso: Optional[str] = "No hay retroalimentacion"


class CambioEstadoRetroalimentacion(BaseModel):
    idsolicitud: Optional[int]
    idresponsablesolicitud: Optional[int]
    idestadosolicitud: Optional[int]
    toBecario: Optional[bool] = False
    nombreBecario: Optional[str] = None
    retroalimentacionEnProceso: Optional[str]
    retroalimentacionFinalizada: Optional[str]
    retroalimentacionCancelada: Optional[str]
    retroalimentacionRecibida: Optional[str]
    retroalimentacionRechazada: Optional[str]