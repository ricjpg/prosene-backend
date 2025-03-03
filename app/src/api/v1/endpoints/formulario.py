from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status

from ....database.database import get_db
from sqlalchemy.orm import Session

from ....utils.protectRoute import get_current_user
from ....schemas.formulario import FormularioCreate, FormularioOutput
from ....schemas.caracteristicasEducativas import CaracteristicasEducativasCreate, CaracteristicasEducativasOutput
from ....schemas.comunicacion import ComunicacionCreate, ComunicacionOutput
from ....schemas.deficiencia import DeficienciaCreate, DeficienciaOutput
from ....schemas.discapacidad import DiscapacidadCreate, DiscapacidadOutput
from ....schemas.movilizacion import MovilizacionCreate, MovilizacionOutput
from ....schemas.servicios import ServiciosCreate, ServiciosOutput

from ....service.formularioService import FormularioService


router = APIRouter(tags=["form"])

@router.post("/inscripcion", status_code=200, summary="Crear nuevo formulario")
async def create_formulario(formulario_input : FormularioCreate, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).create_formulario(formulario_data=formulario_input)
    except Exception as error:
        print(error)
        return HTTPException(status_code=208)

@router.post("/caracteristicas", status_code=200, summary="formulario de caracteristicas educativas")
async def create_caracteristicas(caracteristicas_input : CaracteristicasEducativasCreate, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).create_caracteristicas(caracteristicas_data=caracteristicas_input)
    except Exception as error:
        print(error)
        return HTTPException(status_code=208)

@router.post("/comunicacion", status_code=200, summary="formulario de comunicacion")
async def create_comunicacion(comunicacion_input : ComunicacionCreate, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).create_comunicacion(comunicacion_data=comunicacion_input)
    except Exception as error:
        print(error)
        return HTTPException(status_code=208)

@router.post("/deficiencia", status_code=200, summary="formulario de deficiencia")
async def create_deficiencia(deficiencia_input : DeficienciaCreate, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).create_deficiencia(deficiencia_data=deficiencia_input)
    except Exception as error:
        print(error)
        return HTTPException(status_code=208)

@router.post("/discapacidad", status_code=200, summary="formulario de discapacidad")
async def create_discapacidad(formulario_input : DiscapacidadCreate, session : Session = Depends(get_db)) :
    try:
        return FormularioService(session=session).create_discapacidad(discapacidad_data=formulario_input)
    except Exception as error:
        print(error)
        return HTTPException(status_code=208)

@router.post("/movilizacion", status_code=200, summary="formulario de movilizacion")
async def create_movilizacion(movilizacion_input : MovilizacionCreate, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).create_movilizacion(movilizacion_data=movilizacion_input)
    except Exception as error:
        return HTTPException(status_code=208)

@router.post("/servicio", status_code=200, summary="formulario de servicios")
async def create_servicios(servicio_input : ServiciosCreate, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).create_servicios(servicios_data=servicio_input)
    except Exception as error:
        print(error)
        return HTTPException(status_code=208)

@router.get("/full/{id_usuario}", status_code=200, summary="Obtener formulario completo por id de usuario")
async def get_full_form(id_usuario : int, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).get_full_form_by_id(id_usuario)
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)

