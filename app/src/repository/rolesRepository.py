from .base import BaseRepository
from ..models.role import Role
from ..models.user import User  # Importa el modelo de Usuarios
from ..schemas.roles import RolesCreate, RolesOutput
from fastapi import HTTPException


class RolesRepository(BaseRepository):
    def get_all_roles(self)->list[RolesOutput]:
        roles = self.session.query(Role).all()
        if roles:
            return roles
        return HTTPException(status_code=404, detail="No hay roles")
    
    def get_users_by_roles(self, role_ids: list[int]) -> list[User]:
        """ Obtiene los usuarios que tienen ciertos roles """
        usuarios = self.session.query(User).filter(User.role_id.in_(role_ids)).all()
        
        if not usuarios:
            raise HTTPException(status_code=404, detail="No hay usuarios con los roles especificados")
        
        return usuarios