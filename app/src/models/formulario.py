from datetime import date
import datetime, enum
from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .user import User
from .nacionalidades import Nacionalidades
from .condicionMedica import CondicionMedica


class EstadoCivil(enum.Enum):
    soltero = "soltero"
    casado = "casado"
    viudo = "viudo"
    divorciado = "divorciado"


class Formulario(Base):
    __tablename__ = "formulario"
    idformulario = Column(Integer, primary_key=True, index=True)
    idusuario = Column(Integer, ForeignKey('usuario.idusuario'))
    idcondicionmedica = Column(Integer, ForeignKey("condicionmedica.idcondicionmedica"))
    idnacionalidad = Column(Integer, ForeignKey("nacionalidades.idnacionalidad"))
    estadocivil = Column(Enum(EstadoCivil))
    lugardeprocedencia = Column(String(200))
    direccionactual = Column(String(200))
    perteneceaasociacion = Column(Boolean)
    nombreasociacion = Column(String(100))
    rolenlaasociacion = Column(String(100))
    tienetrabajo = Column(Boolean)
    lugartrabajo = Column(String(150))
    puestotrabajo = Column(String(100))
    direcciontrabajo = Column(String(200))
    telefonotrabajo = Column(String(50))
    ingresomensual = Column(Integer)
    constitucionnucleofamiliar = Column(String(50))
    ocupaciondepadresenhogar = Column(String(100))
    niveleducativopadres = Column(String(100))
    ingresomensualfamiliar = Column(Integer)

    usuario = relationship("User", uselist=False)
    condicionmedica = relationship("CondicionMedica")
    nacionalidades = relationship("Nacionalidades")