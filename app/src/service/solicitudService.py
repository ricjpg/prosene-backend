from sqlalchemy.orm import Session
from ..repository.solicitudRepository import SolicitudRepository
from ..schemas.solicitudes import SolicitudesOutput, SolicitudesCreate
from fastapi import HTTPException

class SolicitudService:
    def __init__(self, session : Session):
        self.__solicitudRepositoy = SolicitudRepository(session=session)


    def create_solicitud(self, solicitud_details: SolicitudesCreate)->SolicitudesOutput:
        return self.__solicitudRepositoy.create_solicitud(solicitud_details)
    