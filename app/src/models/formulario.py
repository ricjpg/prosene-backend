from datetime import date
import datetime
from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .nacionalidades import Nacionalidades
from .condicionMedica import CondicionMedica


class Formulario(Base):
    __tablename__ = "formulario"
    idFormulario = Column(Integer, primary_key=True, index=True)
    idCondicionMedica = Column(Integer, ForeignKey("condicionMedica.idCondicionMedica"))
    nacionalidad = Column(Integer, ForeignKey("nacionalidades.idnacionalidad"))
    estadoCivil = Column(String(50))
    lugarDeProcedencia = Column(String(50))
    direccionActual = Column(String(50))
    perteneceAAsociacion = Column(bool)
    nombreAsociacion = Column(String(50))
    rolEnLaAsociacion = Column(String(50))
    tieneTrabajo = Column(bool)
    lugarTrabajo = Column(String(50))
    puestoTrabajo = Column(String(50))
    direccionTrabajo = Column(String(50))
    telefonoTrabajo = Column(String(50))
    ingresoMensual = Column(Integer)
    constitucionNucleoFamiliar = Column(String(50))
    ocupacionDePadresEnHogar = Column(String(50))
    nivelEducativoPadres = Column(String(50))
    ingresoMensualFamiliar = Column(Integer)

    condicionmedica = relationship("CondicionMedica")
    nacionalidades = relationship("Nacionalidades")