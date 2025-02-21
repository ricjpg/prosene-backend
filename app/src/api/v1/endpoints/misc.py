from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput, UserInUpdate
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....utils.protectRoute import get_current_user
from ....service.rolesService import RolesService
from ....schemas.solicitudes import SolicitudesCreate, SolicitudesOutput, SolicitudUpdate, SolicitudEditar  
from ....schemas.roles import RolesOutput


router = APIRouter(tags=["varios"])

@router.get("/roles", status_code=200, summary="roles creados")
async def get_all(session : Session = Depends(get_db)) -> list[RolesOutput]:
    try:
        return RolesService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error