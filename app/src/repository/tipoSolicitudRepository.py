from .base import BaseRepository
from ..models.tipoSolicitud import TipoSolicitud
from ..schemas.tipoSolicitud import TipoSolicitudOutput
from fastapi import HTTPException


class TipoSolicitudRespository(BaseRepository):
    def get_all_tipos(self)->list[TipoSolicitudOutput]:
        tipoSolicitud = self.session.query(TipoSolicitud).all()
        if tipoSolicitud:
            return tipoSolicitud
        return HTTPException(status_code=404, detail="No hay tipos de solicitud disponibles")