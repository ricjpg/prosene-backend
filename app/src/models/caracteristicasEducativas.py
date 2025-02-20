from datetime import date
from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from .formulario import Formulario

class CaracteristicasEducativas(Base):
    __tablename__ = "caracteristicaseducativas"
    idcaracteristicas = Column(Integer, primary_key=True, index=True)
    idformulario = Column(Integer, ForeignKey("formulario.idformulario"))
    titulonivelmedio = Column(String(100))
    institutoeducativo = Column(String(150))
    fechaegresado = Column(Date)
    estudiaenunah = Column(Boolean)
    carrera = Column(String(150))
    numerodecuenta = Column(String(50))
    puntuacionpaarv = Column(Integer)
    puntuacionpaarm = Column(Integer)
    
    formulario = relationship("Formulario")