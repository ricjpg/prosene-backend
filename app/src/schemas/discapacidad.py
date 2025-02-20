from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
# from .formulario import FormularioOutput
from .escala import Escala



class DiscapacidadCreate(BaseModel):
    idformulario: Optional[int]
    dificultadparaleer: Optional[Escala]
    dificultadparaescribir: Optional[Escala]
    dificultadparaentenderyseguirordenes: Optional[Escala]
    dificultadparamanteneratencion: Optional[Escala]
    dificultadparamemorizarinformacion: Optional[Escala]
    dificultadparaconversaciones: Optional[Escala]
    dificultadpararelacionarseconotros: Optional[Escala]
    dificultadparamatematicas: Optional[Escala]
    dificultadparavidadiaria: Optional[Escala]

    class Config:
        orm_mode = True

class DiscapacidadOutput(BaseModel):
    idformulario: Optional[int]
    dificultadparaleer: Optional[Escala]
    dificultadparaescribir: Optional[Escala]
    dificultadparaentenderyseguirordenes: Optional[Escala]
    dificultadparamanteneratencion: Optional[Escala]
    dificultadparamemorizarinformacion: Optional[Escala]
    dificultadparaconversaciones: Optional[Escala]
    dificultadpararelacionarseconotros: Optional[Escala]
    dificultadparamatematicas: Optional[Escala]
    dificultadparavidadiaria: Optional[Escala]

    class Config:
        orm_mode = True
    

