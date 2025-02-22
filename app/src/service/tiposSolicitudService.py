from sqlalchemy.orm import Session
from ..repository.tipoSolicitudRepository import TipoSolicitudRespository
from ..schemas.tipoSolicitud import TipoSolicitudOutput
from fastapi import HTTPException

class TipoSolicitudService:
    def __init__(self, session : Session):
        self.__tipoSolicitudRepository = TipoSolicitudRespository(session=session)

    def get_all(self)->list[TipoSolicitudOutput]:
        return self.__tipoSolicitudRepository.get_all_tipos()