from datetime import date
import datetime
from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped


class Persona(Base):
    __tablename__ = "persona"
    idpersona = Column(Integer, primary_key = True)
    idusuario = Column(Integer, ForeignKey('usuario.idusuario'))
    numeroidentidad = Column(String(30), unique=True)
    primernombre = Column(String(50))
    segundonombre = Column(String(50))
    primerapellido = Column(String(50))
    segundoapellido = Column(String(50))
    direccion = Column(String(150))
    telefono = Column(String(50))
    fechanacimiento = Column()
    sexo = Column(String(20))
    
    
    usuario = relationship("User", back_populates="persona")
    
    class Config:
        orm_mode = True