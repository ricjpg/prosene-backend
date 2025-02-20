from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
# from .formulario import FormularioOutput


class DeficienciaCreate(BaseModel):
    idformulario: Optional[int]
    hipoacusia: Optional[str]
    sordera: Optional[str]
    bajavision: Optional[str]
    movilidadreducidamiembrosinferiores: Optional[str]
    movilidadreducidamiembrossuperiores: Optional[str]

    class Config:
        orm_mode = True

class DeficienciaOutput(BaseModel):
    idformulario: Optional[int]
    hipoacusia: Optional[str]
    sordera: Optional[str]
    bajavision: Optional[str]
    movilidadreducidamiembrosinferiores: Optional[str]
    movilidadreducidamiembrossuperiores: Optional[str]

    class Config:
        orm_mode = True
    

