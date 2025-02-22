from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
# from .formulario import FormularioOutput
from .escala import Escala



class ServiciosCreate(BaseModel):
    idformulario: Optional[int]
    apoyoenprocesodeadmision: Optional[bool]
    apoyoenpaa: Optional[bool]
    orientaciongeneral: Optional[bool]
    orientacionvocacional: Optional[bool]
    coordinacionconprofesores: Optional[bool]
    orientacionymovilidad: Optional[bool]
    transcripcionalbraille: Optional[bool]
    lecturaygrabaciondetexto: Optional[bool]
    tutorialdemateria: Optional[bool]
    serviciodenotarios: Optional[bool]
    interpretesdelenguadesenias: Optional[bool]
    adecuaciondeaccesoalentorno: Optional[bool]
    otrosservicios: Optional[str]
    barrerasparaestudiarenunah: Optional[str]

    class Config:
        orm_mode = True

class ServiciosOutput(BaseModel):
    idservicio: Optional[int]
    idformulario: Optional[int]
    apoyoenprocesodeadmision: Optional[bool]
    apoyoenpaa: Optional[bool]
    orientaciongeneral: Optional[bool]
    orientacionvocacional: Optional[bool]
    coordinacionconprofesores: Optional[bool]
    orientacionymovilidad: Optional[bool]
    transcripcionalbraille: Optional[bool]
    lecturaygrabaciondetexto: Optional[bool]
    tutorialdemateria: Optional[bool]
    serviciodenotarios: Optional[bool]
    interpretesdelenguadesenias: Optional[bool]
    adecuaciondeaccesoalentorno: Optional[bool]
    otrosservicios: Optional[str]
    barrerasparaestudiarenunah: Optional[str]

    class Config:
        orm_mode = True
    

