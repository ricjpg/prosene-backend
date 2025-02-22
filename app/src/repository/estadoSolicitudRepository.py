from .base import BaseRepository
from ..models.estadoSolicitud import EstadoSolicitud
from ..schemas.estadoSolicitud import EstadoSolicitudOutput
from fastapi import HTTPException


class EstadoSolicitudRepository(BaseRepository):
    def get_all_estados(self)->list[EstadoSolicitudOutput]:
        estadoSolicitud = self.session.query(EstadoSolicitud).all()
        if estadoSolicitud:
            return estadoSolicitud
        return HTTPException(status_code=404, detail="No hay estados de solicitud")