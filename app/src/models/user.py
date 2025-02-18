from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, MappedColumn, mapped_column
from .role import Role
from .centroregional import CentroRegional
from .persona import Persona

class User(Base):
    
    __tablename__ = "usuario"
    idusuario = Column(Integer, primary_key = True)
    email = Column(String(100), unique=True)
    password = Column(String(250))
    role_id = Column(Integer, ForeignKey('roles.idrol'))
    idcentroregional = Column(Integer, ForeignKey('centroregional.idcentroregional'))
    isactive = Column() 
    correoverificado = Column()
    primeracceso = Column()

    role = relationship("Role")
    centroregional = relationship("CentroRegional")
    persona = relationship("Persona", uselist=False)
