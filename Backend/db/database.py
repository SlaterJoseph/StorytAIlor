from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

from .base import Base
from config import settings

from models.User import User
from models.Story import Story
from models.Chapter import Chapter

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()