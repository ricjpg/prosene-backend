from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .formulario import Formulario


class Discapacidad(Base):
    __tablename__ = "discapacidad"
    iddiscapacidad = Column(Integer, primary_key=True, index=True)
    idformulario = Column(Integer, ForeignKey("formulario.idformulario"))
    dificultadparaleer = Column(Enum(Escala))
    dificultadparaescribir = Column(Enum(Escala))
    dificultadparaentenderyseguirordenes = Column(Enum(Escala))
    dificultadparamanteneratencion = Column(Enum(Escala))
    dificultadparamemorizarinformacion = Column(Enum(Escala))
    dificultadparaconversaciones = Column(Enum(Escala))
    dificultadpararelacionarseconotros = Column(Enum(Escala))
    dificultadparamatematicas = Column(Enum(Escala))
    dificultadparavidadiaria = Column(Enum(Escala))

    formulario = relationship("Formulario")