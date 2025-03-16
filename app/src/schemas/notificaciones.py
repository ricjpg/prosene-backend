from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional
from .solicitudes import SolicitudesOutput

class NotificacionCreate(BaseModel):
    idnotificacion: Optional[int]
    idsolicitud: Optional[int]
    isread: Optional[bool] = False
    idusuario: Optional[int]
    create_date: Optional[date] = date.today()
    update_date: Optional[date] = date.today()
    
    
class NotificacionOutput(BaseModel):
    idnotificacion: Optional[int]
    idusuario: Optional[int]
    isread: Optional[bool]
    create_date: Optional[date]
    update_date: Optional[date]
    solicitudes: Optional[SolicitudesOutput]

class DeleteNotificationResponse(BaseModel):
    mensaje: str