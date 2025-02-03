from ..database.database import engine, Base
from ..models import user

def create_tables():
    Base.metadata.create_all(bind=engine)