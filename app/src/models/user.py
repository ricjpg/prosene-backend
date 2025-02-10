from ..database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, MappedColumn, mapped_column
from .role import Role

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50))
    # first_name: Mapped[str] = mapped_column(String(250))
    last_name = Column(String(80))
    email = Column(String(100), unique=True)
    password = Column(String(250))
    role_id = Column(Integer, ForeignKey('roles.id'))
    isActive = Column()

    role = relationship("Role")