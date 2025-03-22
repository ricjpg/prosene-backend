from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput, UserInUpdate
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....utils.protectRoute import get_current_user
from ....service.solicitudService import SolicitudService
from ....schemas.solicitudes import SolicitudesCreate, SolicitudesOutput, SolicitudUpdate, SolicitudEditar, AsignarSchema
from ....schemas.notificaciones import NotificacionCreate, NotificacionOutput
from ....service.solicitudService import SolicitudesCreate

router = APIRouter(tags=["solicitudes"])


@router.post("/nueva", status_code=200, summary="Crear nueva solicitud")
async def create_solicitud(solicitud_input : SolicitudesCreate, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> SolicitudesOutput:
    try:
        solicitud_input.idusuariosolicitante = user.idusuario
        solicitud = SolicitudService(session=session).create_solicitud(solicitud_details=solicitud_input)
        return solicitud
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
        solicitudes = SolicitudService(session=session).obtener_mis_solicitudes(usuario_id)
        if solicitudes:
            return solicitudes
    except Exception as error:
        print(error)
        raise error
    
    
@router.get("/get/{solicitud_id}", status_code=200, summary="obtener solicitud por id solicitud")
async def obtener_notificacion(solicitud_id:int, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> SolicitudesOutput:
    try:
        solicitud = SolicitudService(session=session).get_solicitud_por_id(solicitud_id)
        usuario_id = user.idusuario
        if solicitud.idusuariosolicitante == usuario_id or user.role_id==1 or user.role_id==2:
            return solicitud
        raise HTTPException(status_code=401)
    except Exception as error:
        print(error)
        raise error
    
    
@router.get("/all", status_code=200, summary="Todas las solicitudes hechas")
async def get_all(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user))->list[SolicitudesOutput]:
    if user.role_id == 1 or user.role_id == 2:
        try:
            response = SolicitudService(session=session).get_all()
            return response
        except Exception as error:
            # print(error)
            return HTTPException(status_code=500)
    raise HTTPException(status_code=401)
    
    
@router.get("/tipo/{id}", status_code=200, summary="solicitudes por tipo")
async def obtener_por_tipo(id:int, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[SolicitudesOutput]:
    try:
        return SolicitudService(session=session).get_solicitudes_por_tipo(tipo_id=id)
    except Exception as error:
        print(error)
        raise error
    
    
@router.get("/estado/{estado_id}", status_code=200, summary="solicitudes po estado")
async def obtener_por_estado(estado_id:int, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[SolicitudesOutput]:
    try:
        return SolicitudService(session=session).get_solicitudes_por_estado(estado_id)
    except Exception as error:
        print(error)
        raise error
    
    
@router.put("/editar", status_code=200, summary="solicitudes po estado")
async def obtener_por_estado(solicitudUpdate:SolicitudEditar, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> SolicitudesOutput:
    try:
        return SolicitudService(session=session).editar_solicitud(solicitudUpdate)
    except Exception as error:
        print(error)
        raise error
    
@router.put("/asignar", status_code=200, summary="Asignar solicitud a un colaborador")
async def asignar_solicitud(data: AsignarSchema, session: Session = Depends(get_db), user : UserOutput = Depends(get_current_user))-> SolicitudesOutput:
    try:
        return SolicitudService(session=session).asignar_solicitud(data)
    except Exception as error:
        raise error

@router.delete("/eliminar", status_code=200, summary="Eliminar notificacion")
async def elimnar_notificacion(id:int, session: Session = Depends(get_db), user: UserOutput = Depends(get_current_user))->str:
    try:
        solicitud = SolicitudService(session=session).get_solicitud_por_id(id)
        if not solicitud:
            raise HTTPException(status_code=404,  detail="No existe la solicitud con id: "+str(id))
        if solicitud.idusuariosolicitante == user.idusuario:
            return SolicitudService(session=session).eliminar_solicitud(id)
        raise HTTPException(status_code=401)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@router.get("/atendidas", status_code=200, summary="solicitudes atendidas")
async def obtener_mis_solicitudes_atendidas(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[SolicitudesOutput]:
    try:
        usuario_id = user.idusuario
        solicitudes = SolicitudService(session=session).get_solicitudes_atendidas(usuario_id)
        if solicitudes:
            return solicitudes
    except Exception as error:
        print(error)