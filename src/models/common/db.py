import os

from sqlmodel import Session, create_engine

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = Session(engine)
