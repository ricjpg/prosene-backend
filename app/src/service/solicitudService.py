from sqlalchemy.orm import Session
from datetime import date
from ..repository.solicitudRepository import SolicitudRepository
from ..repository.notificacionesRepository import NotificacionesRepository
from ..schemas.solicitudes import SolicitudesOutput, SolicitudesCreate, SolicitudUpdate, SolicitudEditar
from ..schemas.notificaciones import NotificacionCreate, NotificacionOutput
from fastapi import HTTPException

class SolicitudService:
    def __init__(self, session : Session):
        self.__solicitudRepositoy = SolicitudRepository(session=session)
        self.__notificacionesRepository = NotificacionesRepository(session=session)

    def create_solicitud(self, solicitud_details: SolicitudesCreate)->SolicitudesOutput:
        nueva_solicitud = self.__solicitudRepositoy.create_solicitud(solicitud_details)
        notificacion_data = {
             'idsolicitud' : nueva_solicitud.idsolicitud,
             'idusuario' : nueva_solicitud.idusuariosolicitante,
             'isread' : False,
             'create_date' : date.today(),
             'update_date' : date.today(),
        }
        self.__notificacionesRepository.create_notificacion(notificacion_data)
        return nueva_solicitud
    
    def create_notificacion(self, notificacion_data: NotificacionCreate)->NotificacionOutput:
        nueva_notificacion = self.__notificacionesRepository.create_notificacion(notificacion_data)
        return nueva_notificacion

    def solicitud_cambio_estado(self, nueva_data: SolicitudUpdate) -> SolicitudesOutput:
        solicitud = self.__solicitudRepositoy.get_solicitud_by_id(nueva_data.idsolicitud)
        print(solicitud.idusuariosolicitante)
        data_notificacion = {
                'idsolicitud': nueva_data.idsolicitud,
                'isread': False,
                'idusuario': 1,
                'create_date': date.today(),
                'update_date': date.today()
        }
        self.__notificacionesRepository.create_notificacion(data_notificacion)
        return self.__solicitudRepositoy.solicitud_cambio_estado(nueva_data)
    
    def obtener_mis_solicitudes(self, usuario_id:int)-> list[SolicitudesOutput]:
        solicitudes = self.__solicitudRepositoy.obtener_mis_solicitudes(usuario_id)
        if solicitudes:
            return solicitudes
        raise HTTPException(status_code=404, detail="No tienes solicitudes creadas")
    
    def get_all(self)->list[SolicitudesOutput]:
        return self.__solicitudRepositoy.get_all_solicitudes()
    
    def get_solicitudes_por_estado(self, estado_id:int)-> list[SolicitudesOutput]:
        return self.__solicitudRepositoy(estado_id)
    
    def get_solicitudes_por_tipo(self, tipo_id:int ) ->list[SolicitudesOutput]:
        solicitudes = self.__solicitudRepositoy.get_solicitudes_por_tipo(tipo_id)
        if solicitudes:
            return solicitudes
        raise HTTPException(status_code=404, detail="no se encontraron solicitudes de este tipo")
    
    def editar_solicitud(self, solicitudUpdate:SolicitudEditar)->SolicitudesOutput:
        # solicitud = self.__solicitudRepositoy.get_solicitud_by_id(solicitudUpdate.idsolicitud)
        # if solicitud:
            return self.__solicitudRepositoy.editar_solicitud(solicitudUpdate)
        # return HTTPException(status_code=404, detail="No se encontro la solicitud")

    def get_solicitud_por_id(self, solicitud_id: int)->SolicitudesOutput:
        return self.__solicitudRepositoy.get_solicitud_by_id(solicitud_id)
    
