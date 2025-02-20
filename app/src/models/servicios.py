from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from .formulario import Formulario


class Servicios(Base):
    __tablename__ = "servicios"
    idservicio = Column(Integer, primary_key=True, index=True)
    idformulario = Column(Integer, ForeignKey("formulario.idformulario"))
    apoyoenprocesodeadmision = Column(Boolean)
    apoyoenpaa = Column(Boolean)
    orientaciongeneral = Column(Boolean)
    orientacionvocacional = Column(Boolean)
    coordinacionconprofesores = Column(Boolean)
    orientacionymovilidad = Column(Boolean)
    transcripcionalbraille = Column(Boolean)
    lecturaygrabaciondetexto = Column(Boolean)
    tutorialdemateria = Column(Boolean)
    serviciodenotarios = Column(Boolean)
    interpretesdelenguadesenias = Column(Boolean)
    adecuaciondeaccesoalentorno = Column(Boolean)
    otrosservicios = Column(String(100))
    barrerasparaestudiarenunah = Column(String(150))
    
    formulario = relationship("Formulario")