from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....utils.protectRoute import get_current_user
from ....service.rolesService import RolesService
from ....schemas.roles import RolesOutput
from ....service.centroRegionalService import CentroRegionalService
from ....schemas.centroRegional import CentroRegionalOutput
from ....schemas.condicionMedica import CondicionMedicaOutput
from ....service.condicionMedicaService import CondicionMedicaService
from ....schemas.nacionalidades import NacionalidadOutput
from ....service.nacionalidadesService import NacionalidadesService
from ....schemas.estadoSolicitud import EstadoSolicitudOutput
from ....service.estadoSolicitudService import EstadoSolicitudService
from ....schemas.tipoSolicitud import TipoSolicitudOutput
from ....service.tiposSolicitudService import TipoSolicitudService


router = APIRouter(tags=["varios"])

@router.get("/roles", status_code=200, summary="Lista de roles disponibles")
async def get_all(session : Session = Depends(get_db)) -> list[RolesOutput]:
    try:
        return RolesService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error
    
@router.get("/centros", status_code=200, summary="Lista de centros regionales")
async def get_all(session : Session = Depends(get_db)) -> list[CentroRegionalOutput]:
    try:
        return CentroRegionalService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error
    
@router.get("/condiciones", status_code=200, summary="Lista de condiciones medicas")
async def get_all(session : Session = Depends(get_db)) -> list[CondicionMedicaOutput]:
    try:
        return CondicionMedicaService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error
        
@router.get("/nacionalidades", status_code=200, summary="Lista de nacionalidades")
async def get_all(session : Session = Depends(get_db)) -> list[NacionalidadOutput]:
    try:
        return NacionalidadesService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error

@router.get("/estados", status_code=200, summary="Lista de estados de solicitud")
async def get_all(session : Session = Depends(get_db)) -> list[EstadoSolicitudOutput]:
    try:
        return EstadoSolicitudService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error

@router.get("/tipos", status_code=200, summary="Lista de tipos de solicitud")
async def get_all(session : Session = Depends(get_db)) -> list[TipoSolicitudOutput]:
    try:
        return TipoSolicitudService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error

