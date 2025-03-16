from pydantic import EmailStr, BaseModel
from typing import Union, Optional
from .role import RolInCreate, RolOutput
from .centroRegional import CentroRegionalOutput
from .roles import RolesOutput, RolesCreate
from .persona import PersonaOutput


class UserInCreate(BaseModel):
    email: EmailStr
    password: str
    role_id: Optional[int] = 3
    isactive: Union[bool, None] = True
    idcentroregional: Optional[int] = 1
    correoverificado: Optional[bool] = False
    primeracceso: Optional[bool] = True

    class Config:
        orm_mode = True

class UserOutput(BaseModel):
    idusuario: Optional[int]
    email: Union[EmailStr, None] = None
    role_id: Optional[int] = None
    isActive: Union[bool, None] = True
    correoverificado: Optional[bool] = None
    primeracceso: Optional[bool] = None
    centroregional: Optional[CentroRegionalOutput] = None
    persona: Optional[PersonaOutput] = None

    class Config:
        orm_mode = True

class UserInUpdate(BaseModel):
    email: Union[EmailStr, None] = None
    # password: Union[str, None] = None
    role_id: Union[int, None] = 3
    isActive: Union[bool, None] = True
    idcentroregional: Optional[int] = 1

    class Config:
        orm_mode = True

class UserInLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class UserWithToken(BaseModel):
    token: str
    idusuario: Optional[int] = None
    role_id: Optional[int] = None
    isActive: Union[bool, None] = True

class UserOutputMinimal(BaseModel):
    email: Optional[EmailStr] = None


class ResetPassword(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str] = "password"

    class Config:
        orm_mode = True

class PasswordChange(BaseModel):
    password: str

    class Config:
        orm_mode = True