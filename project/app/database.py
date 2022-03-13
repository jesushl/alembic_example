from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# settings
from app.settings import get_settings

settings = get_settings()

databae_url = settings.database_url
engine = create_engine(
    databae_url, 
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():   
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
