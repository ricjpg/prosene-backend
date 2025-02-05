from ..database.database import Base
from sqlalchemy import Column, Integer, String

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique=True, nullable=False)
    
    class Config:
        orm_mode = True