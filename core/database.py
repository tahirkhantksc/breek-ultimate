# core/database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Example model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

# Setup the database engine and session
DATABASE_URL = "sqlite:///./test.db"  # Change this to your database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
def init_db():
    Base.metadata.create_all(bind=engine)