from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
# from .formulario import FormularioOutput


class CaracteristicasEducativasCreate(BaseModel):
    idformulario: Optional[int]
    titulonivelmedio: Optional[str]
    institutoeducativo: Optional[str]
    fechaegresado: Optional[date]
    estudiaenunah: Optional[bool]
    carrera: Optional[str]
    numerodecuenta: Optional[str]
    puntuacionpaarv: Optional[int]
    puntuacionpaarm: Optional[int]

    class Config:
        orm_mode = True

class CaracteristicasEducativasOutput(BaseModel):
    idcaracteristicas: Optional[int]
    idformulario: Optional[int]
    titulonivelmedio: Optional[str]
    institutoeducativo: Optional[str]
    fechaegresado: Optional[date]
    estudiaenunah: Optional[bool]
    carrera: Optional[str]
    numerodecuenta: Optional[str]
    puntuacionpaarv: Optional[int]
    puntuacionpaarm: Optional[int]

    class Config:
        orm_mode = True
    

