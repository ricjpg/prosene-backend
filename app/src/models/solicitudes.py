import datetime
from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .tipoSolicitud import TipoSolicitud
from .estadoSolicitud import EstadoSolicitud
from .user import User

class Solicitudes(Base):
    __tablename__ = "solicitudes"
    idsolicitud = Column(Integer, primary_key = True)
    fechacreacion = Column(TIMESTAMP, default=datetime.datetime.now(), nullable=False)
    descripcion = Column(String(500))
    toBecario = Column(Boolean)
    nombreBecario = Column(String(150))
    retroalimentacionEnProceso = Column(String(500))
    retroalimentacionRecibida = Column(String(500))
    retroalimentacionCancelada = Column(String(500))
    retroalimentacionFinalizada = Column(String(500))
    retroalimentacionRechazada = Column(String(500))
    
    idusuariosolicitante = Column(Integer, ForeignKey('usuario.idusuario'))
    idresponsablesolicitud = Column(Integer, ForeignKey('usuario.idusuario'))
    idestadosolicitud = Column(Integer, ForeignKey('estadosolicitud.idestadosolicitud'))
    idtiposolicitud = Column(Integer, ForeignKey('tiposolicitud.idtiposolicitud'))

    usuariosolicitante = relationship("User", foreign_keys=[idusuariosolicitante])
    responsablesolicitud = relationship("User", foreign_keys=[idresponsablesolicitud])
    estadosolicitud = relationship("EstadoSolicitud")
    tiposolicitud = relationship("TipoSolicitud")

    class Config:
        orm_mode = True