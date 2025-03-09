from .base import BaseRepository
from fastapi import HTTPException
from ..models.solicitudes import Solicitudes
from ..schemas.solicitudes import SolicitudesCreate, SolicitudesOutput, SolicitudUpdate, SolicitudEditar, AsignarSchema
from ..schemas.estadoSolicitud import EstadoSolicitudOutput
from ..models.tipoSolicitud import TipoSolicitud
from ..models.estadoSolicitud import EstadoSolicitud
from .userRepository import UserRepository
from ..models.user import User


class SolicitudRepository(BaseRepository):
    def create_solicitud(self, solicitud_data : SolicitudesCreate) -> SolicitudesOutput:
        newSolicitud = Solicitudes(**solicitud_data.model_dump(exclude_none=True))
        self.session.add(instance=newSolicitud)
        self.session.commit()
        self.session.refresh(instance=newSolicitud)
        return newSolicitud
    
    def solicitud_cambio_estado(self, nueva_data:SolicitudUpdate) -> SolicitudesOutput:
        solicitud = self.session.query(Solicitudes).filter(Solicitudes.idsolicitud == nueva_data.idsolicitud).first()
        if solicitud:
            solicitud.idestadosolicitud = nueva_data.idestadosolicitud
            solicitud.idresponsablesolicitud = nueva_data.idresponsablesolicitud
            self.session.commit()
            self.session.refresh(instance=solicitud)
            return solicitud
        raise HTTPException(status_code=404, detail="No se encontro la solicitud")
        
    def obtener_mis_solicitudes(self, usuario_id: int) -> list[SolicitudesOutput]:
        solicitudes = self.session.query(Solicitudes).filter(Solicitudes.idusuariosolicitante == usuario_id).all()
        if solicitudes:
            return solicitudes
        raise HTTPException(status_code=404, detail="No se han encontrado tus solicitudes")
    
    def get_all_solicitudes(self)->list[SolicitudesOutput]:
        solicitudes = self.session.query(Solicitudes).all()
        if solicitudes:
            return solicitudes
        raise HTTPException(status_code=404, detail="No hay solicitudes")
    
    def get_solicitudes_por_estado(self, id_estado: int)->list[SolicitudesOutput]:
        estadoSolicitud = self.session.query(Solicitudes).filter(Solicitudes.idestadosolicitud==id_estado).first()
        solicitudes = self.session.query(Solicitudes).filter(Solicitudes.idestadosolicitud==id_estado).all()
        if solicitudes:
            return solicitudes
        raise HTTPException(status_code=404, detail="no hay solicitudes del tipo: "+estadoSolicitud.descripcion)
    
    def get_solicitudes_por_tipo(self, tipo_id:int )->list[SolicitudesOutput]:
        tipoSolicitud = self.session.query(Solicitudes).filter(Solicitudes.idtiposolicitud==tipo_id).first()
        if tipoSolicitud:
            solicitudes = self.session.query(Solicitudes).filter(Solicitudes.idtiposolicitud==tipo_id).all()
            if solicitudes:
                return solicitudes
            raise HTTPException(status_code=404, detail="No hay solicitudes del tipo: "+tipoSolicitud.descripcion)
        raise HTTPException(status_code=404, detail="No existe este tipo de solicitud")
    
    def editar_solicitud(self, solicitud_data: SolicitudEditar) -> SolicitudesOutput:
        solicitudUpdate = self.session.query(Solicitudes).filter(Solicitudes.idsolicitud== solicitud_data.idsolicitud).first()
        if solicitudUpdate:
            solicitudUpdate.descripcion = solicitud_data.descripcion
            solicitudUpdate.idtiposolicitud = solicitud_data.idtiposolicitud
            self.session.commit()
            self.session.refresh(instance=solicitudUpdate)
            return solicitudUpdate
        raise HTTPException(status_code=404, detail="No se encontro la solicitud")
    
    def get_solicitud_by_id(self, solicitud_id:int)->SolicitudesOutput:
        solicitud = self.session.query(Solicitudes).filter(Solicitudes.idsolicitud == solicitud_id).first()
        if solicitud_id:
            return solicitud
        raise HTTPException(status_code=404, detail="No se encontro la solicitud")
                
                
    def asignar_solicitud(self, data: AsignarSchema) ->SolicitudesOutput:
        try:
            solicitud = self.session.query(Solicitudes).filter(Solicitudes.idsolicitud == data.idsolicitud).first()
            usuario = self.session.query(User).filter(User.idusuario == data.idresponsablesolicitud).first()
            if not solicitud:
                raise HTTPException(status_code=404, detail="Solicitud no encontrada")
            if not usuario:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            solicitud.idresponsablesolicitud = usuario.idusuario
            self.session.commit()
            self.session.refresh(solicitud)
            return solicitud
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))
        

    def eliminar_solicitud(self, id:int) ->str:
        try:
            solicitud = self.session.query(Solicitudes).filter(Solicitudes.idsolicitud == id).first()
            if not solicitud:
                raise HTTPException(status_code=404, detail="Solicitud no encontrada")
            self.session.delete(solicitud)
            self.session.commit()
            return "Solicitud eliminada correctamente"
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=str(error))

