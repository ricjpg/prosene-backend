from ..database.database import Base
from sqlalchemy import Column, Integer, String

class CentroRegional(Base):
    __tablename__ = "centroregional"
    idcentroregional = Column(Integer, primary_key = True)
    centroregional = Column(String(100), unique=True, nullable=False)
    
    class Config:
        orm_mode = True