from sqlalchemy.orm import Session
from ..repository.condicionMedicaRepository import CondicionMedicaRepository
from ..schemas.condicionMedica import CondicionMedicaOutput, CondicionMedicaCreate
from fastapi import HTTPException

class CondicionMedicaService:
    def __init__(self, session : Session):
        self.__condicionMedicaRepository = CondicionMedicaRepository(session=session)

    def get_all(self)->list[CondicionMedicaOutput]:
        return self.__condicionMedicaRepository.get_all_condiciones()