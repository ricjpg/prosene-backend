from .base import BaseRepository
from ..models.role import Role
from ..schemas.roles import RolesCreate, RolesOutput
from fastapi import HTTPException


class RolesRepository(BaseRepository):
    def get_all_roles(self)->list[RolesOutput]:
        roles = self.session.query(Role).all()
        if roles:
            return roles
        return HTTPException(status_code=404, detail="No hay roles")