from sqlalchemy.orm import Session
from ..repository.formularioRepository import FormularioRepository
from ..schemas.formulario import FormularioCreate, FormularioOutput
from ..schemas.caracteristicasEducativas import CaracteristicasEducativasCreate, CaracteristicasEducativasOutput
from ..schemas.comunicacion import ComunicacionCreate, ComunicacionOutput
from ..schemas.deficiencia import DeficienciaCreate, DeficienciaOutput
from ..schemas.discapacidad import DiscapacidadCreate, DiscapacidadOutput
from ..schemas.movilizacion import MovilizacionCreate, MovilizacionOutput
from ..schemas.servicios import ServiciosCreate, ServiciosOutput
from fastapi import HTTPException

class FormularioService:
    def __init__(self, session : Session):
        self.__formularioRepository = FormularioRepository(session=session)


    def create_formulario(self, formulario_data: FormularioCreate)->FormularioOutput:
        form = self.__formularioRepository.get_form_by_id(formulario_data.idusuario)
        if not form:
            return self.__formularioRepository.create_formulario(formulario_data)
        raise HTTPException(status_code=208, detail="Este formulario ya existe")
    
    def create_caracteristicas(self, caracteristicas_data: CaracteristicasEducativasCreate)->CaracteristicasEducativasOutput:
        # form = self.__formularioRepository.get_form_by_id(caracteristicas_data.idformulario)
        # if not form:
            return self.__formularioRepository.create_caracteristicas_educativas(caracteristicas_data)
        # raise HTTPException(status_code=208, detail="Este formulario ya existe")
    
    def create_comunicacion(self, comunicacion_data: ComunicacionCreate)->ComunicacionOutput:
        # form = self.__formularioRepository.get_form_by_id(comunicacion_data.idformulario)
        # if not form:
            return self.__formularioRepository.create_comunicacion(comunicacion_data)
        # raise HTTPException(status_code=208, detail="Este formulario ya existe")
    
    def create_deficiencia(self, deficiencia_data: DeficienciaCreate)->DeficienciaOutput:
        # form = self.__formularioRepository.get_form_by_id(deficiencia_data.idformulario)
        # if not form:
            return self.__formularioRepository.create_deficiencia(deficiencia_data)
        # raise HTTPException(status_code=208, detail="Este formulario ya existe")
    
    def create_discapacidad(self, discapacidad_data: DiscapacidadCreate)->DiscapacidadOutput:
        # form = self.__formularioRepository.get_form_by_id(discapacidad_data.idformulario)
        # if not form:
            return self.__formularioRepository.create_discapacidad(discapacidad_data)
        # raise HTTPException(status_code=208, detail="Este formulario ya existe")
    
    def create_movilizacion(self, movilizacion_data: MovilizacionCreate)->MovilizacionOutput:
        # form = self.__formularioRepository.get_form_by_id(movilizacion_data.idformulario)
        # if not form:
            return self.__formularioRepository.create_movilizacion(movilizacion_data)
        # raise HTTPException(status_code=208, detail="Este formulario ya existe")
    
    def create_servicios(self, servicios_data: MovilizacionCreate)->MovilizacionOutput:
        # form = self.__formularioRepository.get_form_by_id(servicios_data.idformulario)
        # if not form:
            return self.__formularioRepository.create_servicios(servicios_data)
        # raise HTTPException(status_code=208, detail="Este formulario ya existe")
    
    def get_full_form_by_id(self, form_id: int):
        full_form = self.__formularioRepository.get_full_form_by_id(form_id)
        if full_form:
            return full_form
        raise HTTPException(status_code=404, detail="Not found")
    
    def get_form_by_id(self, form_id: int):
        form = self.__formularioRepository.get_form_by_id(form_id)
        if form:
            return form
        raise HTTPException(status_code=404, detail="Not found")
    
    def get_form_by_user_id(self, user_id: int):
        form = self.__formularioRepository.get_full_form_by_user(user_id)
        if form:
            return form
        raise HTTPException(status_code=404, detail="Not found")
    