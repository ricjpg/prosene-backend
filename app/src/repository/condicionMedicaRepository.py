from .base import BaseRepository
from ..models.condicionMedica import CondicionMedica
from ..schemas.condicionMedica import CondicionMedicaCreate, CondicionMedicaOutput
from fastapi import HTTPException


class CondicionMedicaRepository(BaseRepository):
    def get_all_condiciones(self)->list[CondicionMedicaOutput]:
        condiciones = self.session.query(CondicionMedica).all()
        if condiciones:
            return condiciones
        return HTTPException(status_code=404, detail="No hay condiciones medicas")