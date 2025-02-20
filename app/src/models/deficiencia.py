from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .formulario import Formulario

class Deficiencia(Base):
    __tablename__ = "deficiencia"
    iddeficiencia = Column(Integer, primary_key=True, index=True)
    idformulario = Column(Integer, ForeignKey("formulario.idformulario"))
    hipoacusia = Column(String(200))
    sordera = Column(String(200))
    bajavision = Column(String(200))
    movilidadreducidamiembrosinferiores = Column(String(200))
    movilidadreducidamiembrossuperiores = Column(String(200))
    
    formulario = relationship("Formulario")