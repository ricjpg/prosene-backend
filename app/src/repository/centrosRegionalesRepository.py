from .base import BaseRepository
from ..models.centroregional import CentroRegional
from ..schemas.centroRegional import CentroRegionalCreate, CentroRegionalOutput
from fastapi import HTTPException


class CentrosRegionalesRepository(BaseRepository):
    def get_all_centros(self)->list[CentroRegionalOutput]:
        centroRegionales = self.session.query(CentroRegional).all()
        if centroRegionales:
            return centroRegionales
        return HTTPException(status_code=404, detail="No hay centros regionales")