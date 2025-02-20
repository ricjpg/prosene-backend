from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime

class Logs(Base):
    __tablename__ = "logs"
    idLog = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    descripcion = Column(String(250))
