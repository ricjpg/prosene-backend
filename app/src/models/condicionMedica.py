from ..database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .persona import Persona

class CondicionMedica(Base):
    __tablename__ = "condicionmedica"
    idcondicionmedica = Column(Integer, primary_key = True)
    condicionmedica = Column(String(50), unique=True, nullable=False)


    class Config:
        orm_mode = True