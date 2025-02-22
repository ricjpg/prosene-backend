from sqlalchemy.orm import Session
from ..repository.estadoSolicitudRepository import EstadoSolicitudRepository
from ..schemas.estadoSolicitud import EstadoSolicitudOutput
from fastapi import HTTPException

class EstadoSolicitudService:
    def __init__(self, session : Session):
        self.__estadoSolicitudRepository = EstadoSolicitudRepository(session=session)

    def get_all(self)->list[EstadoSolicitudOutput]:
        return self.__estadoSolicitudRepository.get_all_estados()