from sqlalchemy.orm import Session
from ..repository.rolesRepository import RolesRepository
from ..schemas.roles import RolesCreate, RolesOutput
from fastapi import HTTPException

class RolesService:
    def __init__(self, session : Session):
        self.__rolesService = RolesRepository(session=session)

    def get_all(self)->list[RolesOutput]:
        return self.__rolesService.get_all_roles()