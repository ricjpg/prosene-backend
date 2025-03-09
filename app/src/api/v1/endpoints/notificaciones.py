import os
from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status,Request, Form, Response
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput, UserInUpdate, ResetPassword
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....utils.protectRoute import get_current_user
from ....schemas.notificaciones import NotificacionOutput
from ....service.notificacionesService import NotificacionesService
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from ....service.emailService import send_email, welcome_mail
from fastapi.responses import JSONResponse

load_dotenv(override=True)

router = APIRouter(tags=["notificaciones"])

env = Environment(loader=FileSystemLoader("templates"))
    
@router.get("/", status_code=200, summary="mis notificaciones")
async def mis_notificaciones(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[NotificacionOutput]:
    try:
        usuario_id = user.idusuario
        notificaciones = NotificacionesService(session=session).get_my_notificaciones(usuario_id)
        if notificaciones:
            return notificaciones
        raise HTTPException(status_code=404, detail='No tienes ninguna notificacion')
    except Exception as error:
        # print(error)
        raise HTTPException(status_code=404, detail="No tienes notificaciones")
    
@router.get('/{id}', status_code=200, summary="obtener notificacion por id")
async def get_notificacion(id:int,session:Session=Depends(get_db), user : UserOutput = Depends(get_current_user))-> NotificacionOutput:
    try:
        notificacion = NotificacionesService(session=session).get_notificacion(id)
        if notificacion:
            if notificacion.idusuario == user.idusuario:
                return notificacion
    except Exception as error:
        raise HTTPException(status_code=404)
    


@router.put('/{id}', status_code=200, summary="marcar notificacion como leida")
async def mark_as_read(id:int,session:Session=Depends(get_db))->NotificacionOutput:
    try:
        notificacion = NotificacionesService(session=session).get_notificacion(id)
        if notificacion:
            return NotificacionesService(session=session).mark_as_read(id)
    except Exception as error:
        raise HTTPException (status_code=404)
    raise HTTPException(status_code=404)

@router.delete('/delete/{id}', status_code=200, summary="eliminar notificación por id")
async def delete_notification(id:int, session:Session=Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            resultado = NotificacionesService(session=session).delete_notification(id)
            return JSONResponse(content=resultado)
        except Exception as error:
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")
    
@router.get("/admin/", status_code=200, summary="mis notificaciones")    
async def mis_notificaciones_admin(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[NotificacionOutput]:
    try:
        usuario_id = user.idusuario
        notificaciones = NotificacionesService(session=session).get_my_notificaciones_admin(usuario_id)
        if notificaciones:
            return notificaciones
        raise HTTPException(status_code=404, detail='No tienes ninguna notificacion')
    except Exception as error:
        # print(error)
        raise HTTPException(status_code=404, detail="No tienes notificaciones")