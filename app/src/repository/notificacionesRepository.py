from .base import BaseRepository
from ..models.notificaciones import Notificaciones
from ..schemas.notificaciones import NotificacionCreate, NotificacionOutput
from .solicitudRepository import SolicitudRepository
from ..models.solicitudes import Solicitudes
from fastapi import HTTPException


class NotificacionesRepository(BaseRepository):
    def create_notificacion(self, notificacion_data : NotificacionCreate):
        # newNotificacion = Notificaciones(**notificacion_data.model_dump(exclude_none=True))
        newNotificacion = Notificaciones(**notificacion_data)
        self.session.add(instance=newNotificacion)
        self.session.commit()
        self.session.refresh(instance=newNotificacion)
        return newNotificacion

    def get_all_notficiacion_por_usuario(self, idusaurio : int) -> list[NotificacionOutput]:
        notificaciones= self.session.query(Notificaciones).filter(Notificaciones.idusuario==idusaurio).order_by(Notificaciones.update_date).limit(20).all()
        if notificaciones:
            return notificaciones
        raise HTTPException(status_code=404, detail="No tienes notificaciones")
    
    def get_notification_por_id_notificacion(self, id_notificacion)-> NotificacionOutput:
        notificacion = self.session.query(Notificaciones).filter(Notificaciones.idnotificacion==id_notificacion).first()
        if notificacion:
            return notificacion
        raise HTTPException(status_code=404)
    
    def mark_as_read(self, id_notificacion) -> NotificacionOutput:
        notificacion = self.session.query(Notificaciones).filter(Notificaciones.idnotificacion==id_notificacion).first()
        notificacion.isread = True
        self.session.add(instance=notificacion)
        self.session.commit()
        self.session.refresh(instance=notificacion)
        return notificacion
    
    def delete_notification_por_id_notificacion(self, id_notificacion: str) -> str:
        notification = self.session.query(Notificaciones).filter(Notificaciones.idnotificacion == id_notificacion).first()

        if notification is None:
            return "Notificación no encontrada"

        self.session.delete(notification)
        self.session.commit()

        return "Notificación " + str(notification.idnotificacion) + " eliminada"
    

    def get_all_notificacion_por_admin(self) -> list[NotificacionOutput]:
        notificaciones= self.session.query(Notificaciones).join(Solicitudes, Notificaciones.idsolicitud == Solicitudes.idsolicitud).filter(Solicitudes.idestadosolicitud == 1).order_by(Notificaciones.update_date).limit(20).all()
        #solicitudes= self.session.query(Solicitudes).filter(Solicitudes.estadosolicitud==1).order_by(Solicitudes.fechacreacion).limit(20)
        

        if notificaciones:
            return notificaciones
        raise HTTPException(status_code=404, detail="No tienes notificaciones")
    
