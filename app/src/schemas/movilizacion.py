from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import Optional, Union
# from .formulario import FormularioOutput
from .escala import Escala



class MovilizacionCreate(BaseModel):
    idformulario: Optional[int]
    dificultadparaorientarseenentorno: Optional[Escala]
    dificultadparasalvardesniveles: Optional[Escala]
    dificultadparausargradas: Optional[Escala]
    dificultadparaviajarentrasportepublico: Optional[Escala]
    dificultadparasubirybajardelvehiculo: Optional[Escala]
    dificultadparadesplazarsedistancias: Optional[Escala]

    class Config:
        orm_mode = True

class MovilizacionOutput(BaseModel):
    idformulario: Optional[int]
    dificultadparaorientarseenentorno: Optional[Escala]
    dificultadparasalvardesniveles: Optional[Escala]
    dificultadparausargradas: Optional[Escala]
    dificultadparaviajarentrasportepublico: Optional[Escala]
    dificultadparasubirybajardelvehiculo: Optional[Escala]
    dificultadparadesplazarsedistancias: Optional[Escala]

    class Config:
        orm_mode = True
    

