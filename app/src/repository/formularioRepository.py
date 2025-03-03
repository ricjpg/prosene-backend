from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from .base import BaseRepository
from ..models.formulario import Formulario
from ..models.caracteristicasEducativas import CaracteristicasEducativas
from ..models.comunicacion import Comunicacion
from ..models.deficiencia import Deficiencia
from ..models.discapacidad import Discapacidad
from ..models.movilizacion import Movilizacion
from ..models.servicios import Servicios
from ..models.persona import Persona
from ..models.user import User
from .userRepository import UserRepository
from ..schemas.formulario import FormularioCreate, FormularioOutput, FormularioFull
from ..schemas.caracteristicasEducativas import CaracteristicasEducativasCreate, CaracteristicasEducativasOutput
from ..schemas.comunicacion import ComunicacionCreate, ComunicacionOutput
from ..schemas.deficiencia import DeficienciaCreate, DeficienciaOutput
from ..schemas.discapacidad import DiscapacidadCreate, DiscapacidadOutput
from ..schemas.movilizacion import MovilizacionCreate, MovilizacionOutput
from ..schemas.servicios import ServiciosCreate, ServiciosOutput
from ..schemas.persona import PersonaOutput
from ..schemas.user import UserOutput


class FormularioRepository(BaseRepository):
    def create_formulario(self, formulario_data : FormularioCreate) -> FormularioOutput:
        user = self.session.query(Formulario).filter(Formulario.idusuario==formulario_data.idusuario).first()
        if not user:
            newFormulario = Formulario(**formulario_data.model_dump(exclude_none=True))
            self.session.add(instance=newFormulario)
            self.session.commit()
            self.session.refresh(instance=newFormulario)
            return newFormulario
        return Exception("El usuario ya tiene un formulario creado")
    

    def formulario_existe_por_idusuaro(self, user_id: int) -> bool:
        try:
            user = self.session.query(Formulario).filter(Formulario.idusuario==user_id).first()
            return bool(user)
        except Exception as error:
            raise HTTPException(status_code=404)

    def create_caracteristicas_educativas(self, caracteristicas_data: CaracteristicasEducativasCreate) -> CaracteristicasEducativasOutput:
        formulario = self.session.query(CaracteristicasEducativas).filter(CaracteristicasEducativas.idformulario==caracteristicas_data.idformulario).first()
        if not formulario:
            newCaracteristicasEducativas = CaracteristicasEducativas(**caracteristicas_data.model_dump(exclude_none=True))
            self.session.add(instance=newCaracteristicasEducativas)
            self.session.commit()
            self.session.refresh(instance=newCaracteristicasEducativas)
            return newCaracteristicasEducativas
        return Exception("El formulario ya tiene el apartado de CARACTERISTICAS EDUCATIVAS")
    
    def create_comunicacion(self, comunicacion_data: ComunicacionCreate) -> ComunicacionOutput:
        formulario = self.session.query(Comunicacion).filter(Comunicacion.idformulario==comunicacion_data.idformulario).first()
        if not formulario:
            newComunicacion = Comunicacion(**comunicacion_data.model_dump(exclude_none=True))
            self.session.add(instance=newComunicacion)
            self.session.commit()
            self.session.refresh(instance=newComunicacion)
            return newComunicacion
        return Exception("El formulario ya tiene el apartado de COMUNICACION")

    def create_deficiencia(self, deficiencia_data: DeficienciaCreate) -> DeficienciaOutput:
        formulario = self.session.query(Deficiencia).filter(Deficiencia.idformulario==deficiencia_data.idformulario).first()
        if not formulario:
            newDeficiencia = Deficiencia(**deficiencia_data.model_dump(exclude_none=True))
            self.session.add(instance=newDeficiencia)
            self.session.commit()
            self.session.refresh(instance=newDeficiencia)
            return newDeficiencia
        return Exception("El formulario ya tiene apartado de Deficiencia")



    def create_discapacidad(self, discapacidad_data: DiscapacidadCreate) -> DiscapacidadOutput:
        formulario = self.session.query(Discapacidad).filter(Discapacidad.idformulario==discapacidad_data.idformulario).first()
        if not formulario:
            newDiscapacidad = Discapacidad(**discapacidad_data.model_dump(exclude_none=True))
            self.session.add(instance=newDiscapacidad)
            self.session.commit()
            self.session.refresh(instance=newDiscapacidad)
            return newDiscapacidad
        return HTTPException(status_code=208)

    
    def create_movilizacion(self, movilizacion_data: MovilizacionCreate)->MovilizacionOutput:
        formulario = self.session.query(Movilizacion).filter(Movilizacion.idformulario==movilizacion_data.idformulario).first()
        if not formulario:
            newMovilizacion = Movilizacion(**movilizacion_data.model_dump(exclude_none=True))
            self.session.add(instance=newMovilizacion)
            self.session.commit()
            self.session.refresh(instance=newMovilizacion)
            return newMovilizacion
        return HTTPException(status_code=208)
    
    
    def create_servicios(self, servicios_data: ServiciosCreate) -> ServiciosOutput:
        formulario = self.session.query(Servicios).filter(Servicios.idformulario==servicios_data.idformulario).first()
        if not formulario:
            newServicios = Servicios(**servicios_data.model_dump(exclude_none=True))
            self.session.add(instance=newServicios)
            self.session.commit()
            self.session.refresh(instance=newServicios)
            return newServicios
        return Exception("El formulario ya tiene el apartado de SERVICOS")
    
    def get_form_by_id(self, form_id : int) -> FormularioOutput:
        formulario = self.session.query(Formulario).filter(Formulario.idformulario==form_id).first()
        return formulario
    
    def get_full_form_by_id(self, user_id:int) -> FormularioFull:
        try:
            formulario = self.session.query(Formulario).filter(Formulario.idusuario==user_id).first()
            if formulario:
                caracteristicas = self.session.query(CaracteristicasEducativas).filter(CaracteristicasEducativas.idformulario==formulario.idformulario).first()
                comunicacion = self.session.query(Comunicacion).filter(Comunicacion.idformulario==formulario.idformulario).first()
                deficiencia = self.session.query(Deficiencia).filter(Deficiencia.idformulario==formulario.idformulario).first()
                discapacidad = self.session.query(Discapacidad).filter(Discapacidad.idformulario==formulario.idformulario).first()
                movilizacion = self.session.query(Movilizacion).filter(Movilizacion.idformulario==formulario.idformulario).first()
                servicios = self.session.query(Servicios).filter(Servicios.idformulario==formulario.idformulario).first()
                persona = self.session.query(Persona).filter(Persona.idusuario==formulario.idusuario).first()
                usuario = self.session.query(User).filter(User.idusuario == formulario.idusuario).first()
                return {
                    "usuario": usuario,
                    "detalles personales": persona,
                    "formulario": formulario,
                    "caracteristicas": caracteristicas,
                    "comunicacion": comunicacion,
                    "deficiencia": deficiencia,
                    "discapacidad": discapacidad,
                    "movilizacion": movilizacion,
                    "servicios": servicios
                }
            raise HTTPException(status_code=404, detail="No tiene formulario de inscripcion")
        except Exception as error:
            raise HTTPException(status_code=204)
    
    def get_form_by_user_id(self, user_id:int) ->FormularioOutput:
        try:
            formulario = self.session.query(Formulario).filter(Formulario.idformulario==user_id).first()
            return formulario
        except Exception as error:
            raise HTTPException(status_code=204)
    
    def get_full_form_by_user(self, user_id:int) -> FormularioFull:
        try:
            formulario = self.session.query(Formulario).filter(Formulario.idusuario==user_id).first()
            if formulario:
                caracteristicas = self.session.query(CaracteristicasEducativas).filter(CaracteristicasEducativas.idformulario==formulario.idformulario).first()
                comunicacion = self.session.query(Comunicacion).filter(Comunicacion.idformulario==formulario.idformulario).first()
                deficiencia = self.session.query(Deficiencia).filter(Deficiencia.idformulario==formulario.idformulario).first()
                discapacidad = self.session.query(Discapacidad).filter(Discapacidad.idformulario==formulario.idformulario).first()
                movilizacion = self.session.query(Movilizacion).filter(Movilizacion.idformulario==formulario.idformulario).first()
                servicios = self.session.query(Servicios).filter(Servicios.idformulario==formulario.idformulario).first()
                return {
                    "formulario": formulario,
                    "caracteristicas": caracteristicas,
                    "comunicacion": comunicacion,
                    "deficiencia": deficiencia,
                    "discapacidad": discapacidad,
                    "movilizacion": movilizacion,
                    "servicios": servicios
                }
            return HTTPException(status_code=404, detail="Este usuario no tiene formulario de inscripcion")
        except Exception as error:
            raise HTTPException(status_code=204)
