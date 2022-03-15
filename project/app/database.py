from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# settings
from app.settings import get_settings

settings = get_settings()

databae_url = settings.database_url
# TODO: Remove
print(f"DATABASE URL: {database_url}")

engine = create_engine(databae_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def commit(model_obj: Base):
    with get_db() as session:
        session.add(model_obj)
        session.commit()
