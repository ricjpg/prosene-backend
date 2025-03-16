from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
# from .user import UserOutput
from .condicionMedica import CondicionMedicaOutput


class PersonaCreate(BaseModel):
    idusuario: int
    numeroidentidad: str
    primernombre: str
    segundonombre: Optional[str] = None
    primerapellido: str
    segundoapellido: Optional[str] = None
    direccion: str
    telefono: str
    fechanacimiento: Optional[date] = None
    sexo: str
    class Config:
        orm_mode = True
    

class PersonaOutput(BaseModel):
    idpersona: int
    numeroidentidad: str
    primernombre: str
    segundonombre: Optional[str] = None
    primerapellido: str
    segundoapellido: Optional[str] = None
    direccion: str
    telefono: str
    fechanacimiento: Optional[date] = None
    sexo: str
    # usuario: Optional[UserOutput] = None
    class Config:
        orm_mode = True