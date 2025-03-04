from .base import BaseRepository
from ..models.notificaciones import Notificaciones
from ..schemas.notificaciones import NotificacionCreate, NotificacionOutput
from .solicitudRepository import SolicitudRepository
from ..models.solicitudes import Solicitudes


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
        return notificaciones
    
    def get_notification_por_id_notificacion(self, id_notificacion)-> NotificacionOutput:
        notificacion = self.session.query(Notificaciones).filter(Notificaciones.idnotificacion==id_notificacion).first()
        return notificacion
    
    def mark_as_read(self, id_notificacion) -> NotificacionOutput:
        notificacion = self.session.query(Notificaciones).filter(Notificaciones.idnotificacion==id_notificacion).first()
        notificacion.isread = True
        self.session.add(instance=notificacion)
        self.session.commit()
        self.session.refresh(instance=notificacion)
        return notificacion
    