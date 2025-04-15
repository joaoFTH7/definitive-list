import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv("DB_USERNAME", "root")
DB_PASS = os.getenv("DB_PASSWORD", "rootlist")
DB_HOSTNAME = os.getenv("DB_HOSTNAME", "db")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_DATABASE_NAME = os.getenv("DB_DATABASE_NAME","listdb")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
