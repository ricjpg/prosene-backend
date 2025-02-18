from ..database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class EstadoSolicitud(Base):
    __tablename__ = "estadosolicitud"
    idestadosolicitud = Column(Integer, primary_key = True)
    descripcion = Column(String(50), unique=True, nullable=False)

    
    class Config:
        orm_mode = True