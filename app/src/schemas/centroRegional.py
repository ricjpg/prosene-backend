from pydantic import EmailStr, BaseModel
from typing import Optional, Union


class CentroRegionalCreate(BaseModel):
    idcentroregional: int
    centroregional: str
    class Config:
        orm_mode = True
    

class CentroRegionalOutput(BaseModel):
    idcentroregional: int
    centroregional: str
    class Config:
        orm_mode = True