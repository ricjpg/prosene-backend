from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput, UserInUpdate
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....utils.protectRoute import get_current_user
from ....service.solicitudService import SolicitudService
from ....schemas.solicitudes import SolicitudesCreate, SolicitudesOutput, SolicitudUpdate, SolicitudEditar  


router = APIRouter(tags=["solicitudes"])


@router.post("/nueva", status_code=200, summary="Crear nueva solicitud")
async def create_solicitud(solicitud_input : SolicitudesCreate, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> SolicitudesOutput:
    try:
        solicitud_input.idusuariosolicitante = user.idusuario
        return SolicitudService(session=session).create_solicitud(solicitud_details=solicitud_input)
    except Exception as error:
        print(error)
        raise error

@router.put("/atender", status_code=200, summary="cambio de estado")
async def actualizar_estado(nueva_data : SolicitudUpdate, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> SolicitudesOutput:
    try:
        nueva_data.idresponsablesolicitud = user.idusuario
        return SolicitudService(session=session).solicitud_cambio_estado(nueva_data)
    except Exception as error:
        print(error)
        raise error
    

@router.get("/", status_code=200, summary="mis solicitudes")
async def obtener_mis_solicitudes(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[SolicitudesOutput]:
    try:
        usuario_id = user.idusuario
        return SolicitudService(session=session).obtener_mis_solicitudes(usuario_id)
    except Exception as error:
        print(error)
        raise error
    
    
@router.get("/{solicitud_id}", status_code=200, summary="obtener solicitud por id solicitud")
async def obtener_mis_solicitudes(solicitud_id:int, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> SolicitudesOutput:
    try:
        solicitud = SolicitudService(session=session).get_solicitud_por_id(solicitud_id)
        usuario_id = user.idusuario
        if solicitud.idusuariosolicitante == usuario_id:
            return solicitud
        return HTTPException(status_code=401)
    except Exception as error:
        print(error)
        raise error
    
    
@router.get("/all", status_code=200, summary="Todas las solicitudes hechas")
async def get_all(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[SolicitudesOutput]:
    try:
        return SolicitudService(session=session).get_all()
    except Exception as error:
        print(error)
        raise error
    
    
@router.get("/tipo/{id}", status_code=200, summary="solicitudes por tipo")
async def obtener_por_tipo(id:int, session : Session = Depends(get_db)) -> list[SolicitudesOutput]:
    try:
        return SolicitudService(session=session).get_solicitudes_por_tipo(tipo_id=id)
    except Exception as error:
        print(error)
        raise error
    
    
@router.get("/estado/{estado_id}", status_code=200, summary="solicitudes po estado")
async def obtener_por_estado(estado_id:int, session : Session = Depends(get_db)) -> list[SolicitudesOutput]:
    try:
        return SolicitudService(session=session).get_solicitudes_por_estado(estado_id)
    except Exception as error:
        print(error)
        raise error
    
    
@router.put("/editar", status_code=200, summary="solicitudes po estado")
async def obtener_por_estado(solicitudUpdate:SolicitudEditar, session : Session = Depends(get_db)) -> SolicitudesOutput:
    try:
        return SolicitudService(session=session).editar_solicitud(solicitudUpdate)
    except Exception as error:
        print(error)
        raise error
    

