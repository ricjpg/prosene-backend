from .escala import Escala
from ..database.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .formulario import Formulario


class Discapacidad(Base):
    __tablename__ = "discapacidad"
    idDiscapacidad = Column(Integer, primary_key=True, index=True)
    idFormulario = Column(Integer, ForeignKey("formulario.idFormulario"))
    dificultadParaLeer = Column(Enum(Escala))
    dificultadParaEscribir = Column(Enum(Escala))
    dificultadPararEntenderYSeguirOrdenes = Column(Enum(Escala))
    dificultadParaMantenerAtencion = Column(Enum(Escala))
    dificultadParaMemorizarInformacion = Column(Enum(Escala))
    dificultadParaConversaciones = Column(Enum(Escala))
    dificultadParaRelacionarseConOtros = Column(Enum(Escala))
    dificultadParaMatematicas = Column(Enum(Escala))
    dificultadParaVidaDiaria = Column(Enum(Escala))

    formulario = relationship("Formulario")