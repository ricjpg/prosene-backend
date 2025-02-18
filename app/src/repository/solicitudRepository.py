from .base import BaseRepository
from ..models.solicitudes import Solicitudes
from ..schemas.solicitudes import SolicitudesCreate, SolicitudesOutput


class SolicitudRepository(BaseRepository):
    def create_solicitud(self, solicitud_data : SolicitudesCreate) -> SolicitudesOutput:
        
        newSolicitud = Solicitudes(**solicitud_data.model_dump(exclude_none=True))
        
        self.session.add(instance=newSolicitud)
        self.session.commit()
        self.session.refresh(instance=newSolicitud)
        return newSolicitud