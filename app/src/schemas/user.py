from pydantic import EmailStr, BaseModel
from typing import Union, Optional
from .role import RolInCreate


class UserInCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role_id: Union[int, None] = 3
    isActive: Union[bool, None] = True

    class Config:
        orm_mode = True

class UserOutput(BaseModel):
    id: int
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    role_id: Union[int, None] = None
    isActive: Union[bool, None] = True

    class Config:
        orm_mode = True

class UserInUpdate(BaseModel):
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None
    role_id: Union[int, None] = 3
    isActive: Union[bool, None] = True

    class Config:
        orm_mode = True

class UserInLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class UserWithToken(BaseModel):
    token: str