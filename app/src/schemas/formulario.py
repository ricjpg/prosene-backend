from datetime import date, datetime
from pydantic import EmailStr, BaseModel
import enum
from typing import Optional, Union
from .caracteristicasEducativas import CaracteristicasEducativasOutput
from .comunicacion import ComunicacionOutput
from .deficiencia import DeficienciaOutput
from .movilizacion import MovilizacionOutput
from .servicios import ServiciosOutput
from .discapacidad import DiscapacidadOutput

class EstadoCivil(str, enum.Enum):
    soltero = "soltero"
    casado = "casado"
    divorciado = "divorciado"
    viudo = "viudo"


class FormularioCreate(BaseModel):
    idusuario: Optional[int]
    idcondicionmedica: Optional[int]
    idnacionalidad: Optional[int]
    estadocivil: Optional[EstadoCivil]
    lugardeprocedencia: Optional[str]
    direccionactual: Optional[str]
    perteneceaasociacion: Optional[bool]
    nombreasociacion: Optional[str]
    rolenlaasociacion: Optional[str]
    tienetrabajo: Optional[bool]
    lugartrabajo: Optional[str]
    puestotrabajo: Optional[str]
    direcciontrabajo: Optional[str]
    telefonotrabajo: Optional[str]
    ingresomensual: Optional[int]
    constitucionnucleofamiliar: Optional[str]
    ocupaciondepadresenhogar: Optional[str]
    niveleducativopadres: Optional[str]
    ingresomensualfamiliar: Optional[int]


class FormularioOutput(BaseModel):
    idusuario: Optional[int]
    idcondicionmedica: Optional[int]
    idnacionalidad: Optional[int]
    estadocivil: Optional[EstadoCivil]
    lugardeprocedencia: Optional[str]
    direccionactual: Optional[str]
    perteneceaasociacion: Optional[bool]
    nombreasociacion: Optional[str]
    rolenlaasociacion: Optional[str]
    tienetrabajo: Optional[bool]
    lugartrabajo: Optional[str]
    puestotrabajo: Optional[str]
    direcciontrabajo: Optional[str]
    telefonotrabajo: Optional[str]
    ingresomensual: Optional[int]
    constitucionnucleofamiliar: Optional[str]
    ocupaciondepadresenhogar: Optional[str]
    niveleducativopadres: Optional[str]
    ingresomensualfamiliar: Optional[int]

    class Config:
        orm_mode = True
    
class FormularioFull(BaseModel):
    formulario: Optional[FormularioOutput] = None
    caracteristicasEducativas: Optional[CaracteristicasEducativasOutput] = None
    comunicacion: Optional[ComunicacionOutput] = None
    deficiencias: Optional[DeficienciaOutput] = None
    discapacidad: Optional[DiscapacidadOutput] = None
    movilizacion: Optional[MovilizacionOutput] = None
    servicios: Optional[ServiciosOutput] = None
