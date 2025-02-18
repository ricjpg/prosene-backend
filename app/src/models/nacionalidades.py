from ..database.database import Base
from sqlalchemy import Column, Integer, String

class Nacionalidades(Base):
    __tablename__ = "nacionalidades"
    idnacionalidad = Column(Integer, primary_key = True)
    nacionalidad = Column(String(50), unique=True, nullable=False)
    
    class Config:
        orm_mode = True