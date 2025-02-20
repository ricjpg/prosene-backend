from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from .formulario import Formulario


class Comunicacion(Base):
    __tablename__ = "comunicacion"
    idcomunicacion = Column(Integer, primary_key=True)
    idformulario = Column(Integer, ForeignKey("formulario.idformulario"))
    usabraille = Column(Boolean)
    usalsho = Column(Boolean)
    usacomunicaciongestual = Column(Boolean)
    usalecturalabial = Column(Boolean)
    usacomunicaciontotal = Column(Boolean)
    usaacabo = Column(Boolean)
    usodecalculadora = Column(Boolean)
    
    formulario = relationship("Formulario")