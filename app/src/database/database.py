from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv(override=True)

# LOCAL CONECTION
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('DB_USER_LOCAL')}:{os.getenv('DB_PASSWORD_LOCAL')}@localhost:{os.getenv('DB_PORT_LOCAL')}/{os.getenv('DB_SERVER_LOCAL')}"


# REMOTE CONECTION
#SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_SERVER')}?client_encoding=utf8"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()