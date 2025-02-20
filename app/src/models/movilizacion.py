from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .formulario import Formulario


class Movilizacion(Base):
    __tablename__ = "movilizacion"
    idmovilizacion = Column(Integer, primary_key=True, index=True)
    idformulario = Column(Integer, ForeignKey("formulario.idformulario"))
    dificultadparaorientarseenentorno = Column(Enum(Escala))
    dificultadparasalvardesniveles = Column(Enum(Escala))
    dificultadparausargradas = Column(Enum(Escala))
    dificultadparaviajarentrasportepublico = Column(Enum(Escala))
    dificultadparasubirybajardelvehiculo = Column(Enum(Escala))
    dificultadparadesplazarsedistancias = Column(Enum(Escala))
    
    formulario = relationship("Formulario")