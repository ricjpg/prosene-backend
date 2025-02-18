import datetime
from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .tipoSolicitud import TipoSolicitud
from .estadoSolicitud import EstadoSolicitud
from .user import User

class Solicitudes(Base):
    __tablename__ = "solicitudes"
    idsolicitud = Column(Integer, primary_key = True)
    fechacreacion = Column()
    descripcion = Column(String(50))

    # idusuariosolicitante: Mapped[int] = mapped_column(ForeignKey('usuario.idusuario'))
    # idresponsablesolicitud: Mapped[int] = mapped_column(ForeignKey('usuario.idusuario'))


    # idestadosolicitud: Mapped[int] = mapped_column(ForeignKey('estadosolicitud.idestadosolicitud'))
    # idtiposolicitud: Mapped[int] = mapped_column(ForeignKey("tiposolicitud.idtiposolicitud"))
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