import datetime
from datetime import date
from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from .solicitudes import Solicitudes

class Notificaciones(Base):
    __tablename__ = "notificaciones"
    idnotificacion = Column(Integer, primary_key=True, index=True)
    idsolicitud = Column(Integer, ForeignKey("solicitudes.idsolicitud", ondelete="CASCADE"))
    idusuario = Column(Integer, ForeignKey('usuario.idusuario', ondelete="CASCADE"))
    isread = Column(Boolean)
    create_date = Column(TIMESTAMP, default=datetime.datetime.now())
    update_date = Column(TIMESTAMP, default=datetime.datetime.now())
    
    solicitudes = relationship("Solicitudes")