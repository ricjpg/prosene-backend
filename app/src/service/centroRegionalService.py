from sqlalchemy.orm import Session
from ..repository.centrosRegionalesRepository import CentrosRegionalesRepository
from ..schemas.centroRegional import CentroRegionalCreate, CentroRegionalOutput
from fastapi import HTTPException

class CentroRegionalService:
    def __init__(self, session : Session):
        self.__centroRegionalRepository = CentrosRegionalesRepository(session=session)

    def get_all(self)->list[CentroRegionalOutput]:
        return self.__centroRegionalRepository.get_all_centros()