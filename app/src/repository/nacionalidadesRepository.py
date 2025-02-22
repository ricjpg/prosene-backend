from .base import BaseRepository
from ..models.nacionalidades import Nacionalidades
from ..schemas.nacionalidades import NacionalidadOutput
from fastapi import HTTPException


class NacionalidadesRepository(BaseRepository):
    def get_all_nacionalidades(self)->list[NacionalidadOutput]:
        nacionalidades = self.session.query(Nacionalidades).all()
        if nacionalidades:
            return nacionalidades
        return HTTPException(status_code=404, detail="No hay nacionalidades")