from pydantic import EmailStr, BaseModel
from typing import Optional, Union


class CondicionMedicaCreate(BaseModel):
    idcondicionmedica: int
    condicionmedica: str
    class Config:
        orm_mode = True
    

class CondicionMedicaOutput(BaseModel):
    idcondicionmedica: Optional[int]
    condicionmedica: Optional[str]
    class Config:
        orm_mode = True