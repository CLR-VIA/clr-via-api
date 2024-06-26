# Note: the module name is psycopg, not psycopg3
import psycopg
import os
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

POSTGRES_USER: str = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD: str = os.environ["POSTGRES_PASSWORD"]
POSTGRES_DB: str = os.environ["POSTGRES_DB"]
POSTGRES_SERVER: str = os.environ["POSTGRES_HOST"]
POSTGRES_PORT: str = os.environ["POSTGRES_PORT"]

SQLALCHEMY_DATABASE_URL: str = "postgresql+psycopg://{}:{}@{}:{}/{}".format(
    POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT, POSTGRES_DB
)

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal: sessionmaker = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Dependency
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
