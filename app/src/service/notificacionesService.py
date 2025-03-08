from sqlalchemy.orm import Session
from datetime import date
from ..repository.solicitudRepository import SolicitudRepository
from ..repository.notificacionesRepository import NotificacionesRepository
from ..schemas.solicitudes import SolicitudesOutput, SolicitudesCreate, SolicitudUpdate, SolicitudEditar
from ..schemas.notificaciones import NotificacionCreate, NotificacionOutput
from fastapi import HTTPException

class NotificacionesService:
    def __init__(self, session : Session):
        self.__notificacionesRepository = NotificacionesRepository(session=session)


    def get_my_notificaciones(self, usuario_id:int)-> list[NotificacionOutput]:
        solicitudes = self.__notificacionesRepository.get_all_notficiacion_por_usuario(usuario_id)
        if solicitudes:
            return solicitudes
        raise HTTPException(status_code=404, detail="No tienes solicitudes creadas")

    def mark_as_read(self, id_notification:int)->NotificacionOutput:
        notificacion = self.__notificacionesRepository.get_notification_por_id_notificacion(id_notification)
        if notificacion:
            return self.__notificacionesRepository.mark_as_read(id_notification)
        raise HTTPException(status_code=404, detail="No se encontro la notificacion")
    
    def get_notificacion(self, id_notificacion:int)->NotificacionOutput:
        notificacion = self.__notificacionesRepository.get_notification_por_id_notificacion(id_notificacion)
        if notificacion:
            return notificacion
        raise HTTPException(status_code=404, detail="No se encontro la notificacion")
    
    def delete_notification(self, id_notificacion:int):
        resultado = self.__notificacionesRepository.delete_notification_por_id_notificacion(id_notificacion)
    
        if resultado == "Notificación no encontrada":
            raise HTTPException(status_code=404, detail="No se encontró la notificación")

        return {"message": resultado}
    
    def get_my_notificaciones_admin(self, usuario_id:int)-> list[NotificacionOutput]:
        notificaciones = self.__notificacionesRepository.get_all_notificacion_por_admin()
        
        if notificaciones:
            return notificaciones
        raise HTTPException(status_code=404, detail="No tienes notificaciones")