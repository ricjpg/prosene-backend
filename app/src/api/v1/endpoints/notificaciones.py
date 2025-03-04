import os
from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status,Request, Form
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput, UserInUpdate, ResetPassword
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....utils.protectRoute import get_current_user
from ....schemas.notificaciones import NotificacionOutput
from ....service.notificacionesService import NotificacionesService
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from ....service.emailService import send_email, welcome_mail

load_dotenv(override=True)

router = APIRouter(tags=["notificaciones"])

env = Environment(loader=FileSystemLoader("templates"))
    
@router.get("/", status_code=200, summary="mis notificaciones")
async def mis_notificaciones(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)) -> list[NotificacionOutput]:
    try:
        usuario_id = user.idusuario
        return NotificacionesService(session=session).get_my_notificaciones(usuario_id)
    except Exception as error:
        print(error)
        raise error
    
@router.get('/{id}', status_code=200, summary="obtener notificacion por id")
async def get_notificacion(id:int,session:Session=Depends(get_db), user : UserOutput = Depends(get_current_user))->NotificacionOutput:
    notificacion = NotificacionesService(session=session).get_notificacion(id)
    if notificacion.idusuario == user.idusuario:
        try:
            return NotificacionesService(session=session).get_notificacion(id)
        except Exception as error:
            raise error
    return HTTPException(status_code=401, detail="Esta solicitud no te pertenece")
    

@router.put('/{id}', status_code=200, summary="marcar notificacion como leida")
async def mark_as_read(id:int,session:Session=Depends(get_db))->NotificacionOutput:
    try:
        return NotificacionesService(session=session).mark_as_read(id)
    except Exception as error:
        raise error