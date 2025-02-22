from sqlalchemy.orm import Session
from ..repository.nacionalidadesRepository import NacionalidadesRepository
from ..schemas.nacionalidades import NacionalidadOutput
from fastapi import HTTPException

class NacionalidadesService:
    def __init__(self, session : Session):
        self.__nacionalidadesRepository = NacionalidadesRepository(session=session)

    def get_all(self)->list[NacionalidadOutput]:
        return self.__nacionalidadesRepository.get_all_nacionalidades()