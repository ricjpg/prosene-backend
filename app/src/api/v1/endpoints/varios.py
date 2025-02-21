from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....utils.protectRoute import get_current_user
from ....service.rolesService import RolesService
from ....schemas.roles import RolesOutput
from ....service.centroRegionalService import CentroRegionalService
from ....schemas.centroRegional import CentroRegionalOutput


router = APIRouter(tags=["varios"])

@router.get("/roles", status_code=200, summary="roles disponibles")
async def get_all(session : Session = Depends(get_db)) -> list[RolesOutput]:
    try:
        return RolesService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error
    
@router.get("/centros", status_code=200, summary="centros regionales")
async def get_all(session : Session = Depends(get_db)) -> list[CentroRegionalOutput]:
    try:
        return CentroRegionalService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error
    
