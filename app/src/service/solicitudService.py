from sqlalchemy.orm import Session
from ..repository.solicitudRepository import SolicitudRepository
from ..schemas.solicitudes import SolicitudesOutput, SolicitudesCreate, SolicitudUpdate, SolicitudEditar
from fastapi import HTTPException

class SolicitudService:
    def __init__(self, session : Session):
        self.__solicitudRepositoy = SolicitudRepository(session=session)


    def create_solicitud(self, solicitud_details: SolicitudesCreate)->SolicitudesOutput:
        return self.__solicitudRepositoy.create_solicitud(solicitud_details)
    
    def solicitud_cambio_estado(self, nueva_data: SolicitudUpdate) -> SolicitudesOutput:
        return self.__solicitudRepositoy.solicitud_cambio_estado(nueva_data)
    
    def obtener_mis_solicitudes(self, usuario_id:int)-> list[SolicitudesOutput]:
        solicitudes = self.__solicitudRepositoy.obtener_mis_solicitudes(usuario_id)
        if solicitudes:
            return solicitudes
        return HTTPException(status_code=404, detail="No tienes solicitudes creadas")
    
    def get_all(self)->list[SolicitudesOutput]:
        return self.__solicitudRepositoy.get_all_solicitudes()
    
    def get_solicitudes_por_estado(self, estado_id:int)-> list[SolicitudesOutput]:
        return self.__solicitudRepositoy.get_solicitudes_por_estado(estado_id)
    
    def get_solicitudes_por_tipo(self, tipo_id:int ) ->list[SolicitudesOutput]:
        solicitudes = self.__solicitudRepositoy.get_solicitudes_por_tipo(tipo_id)
        if solicitudes:
            return solicitudes
        return HTTPException(status_code=404, detail="no se encontraron solicitudes de este tipo")
    
    def editar_solicitud(self, solicitudUpdate:SolicitudEditar)->SolicitudesOutput:
        # solicitud = self.__solicitudRepositoy.get_solicitud_by_id(solicitudUpdate.idsolicitud)
        # if solicitud:
            return self.__solicitudRepositoy.editar_solicitud(solicitudUpdate)
        # return HTTPException(status_code=404, detail="No se encontro la solicitud")
    
