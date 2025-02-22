from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
# from .formulario import FormularioOutput


class ComunicacionCreate(BaseModel):
    idformulario: Optional[int]
    usabraille: Optional[bool]
    usalsho: Optional[bool]
    usacomunicaciongestual: Optional[bool]
    usalecturalabial: Optional[bool]
    usacomunicaciontotal: Optional[bool]
    usaacabo: Optional[bool]
    usodecalculadora: Optional[bool]

    class Config:
        orm_mode = True

class ComunicacionOutput(BaseModel):
    idcomunicacion: Optional[int]
    idformulario: Optional[int]
    usabraille: Optional[bool]
    usalsho: Optional[bool]
    usacomunicaciongestual: Optional[bool]
    usalecturalabial: Optional[bool]
    usacomunicaciontotal: Optional[bool]
    usaacabo: Optional[bool]
    usodecalculadora: Optional[bool]

    class Config:
        orm_mode = True
    

