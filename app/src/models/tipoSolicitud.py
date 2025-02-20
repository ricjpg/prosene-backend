from ..database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class TipoSolicitud(Base):
    __tablename__ = "tiposolicitud"
    idtiposolicitud = Column('idtiposolicitud',Integer, primary_key = True)
    descripcion = Column('descripcion',String(100), unique=True, nullable=False)

    # solicitudes = relationship("Solicitudes")
    class Config:
        orm_mode = True