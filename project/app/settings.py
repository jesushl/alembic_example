from pydantic import BaseSettings
from functools import lru_cache

# constants from environment
from app.constants import DATABASE_URL
#  sessions data type
from uuid import uuid4

class APPSettings(BaseSettings):
    app_name: str = "Companies"
    admin_email: str = "jesushledon@gmail.com"
    database_url: str = DATABASE_URL
    alphavantage_key: str

    class Config:
        env_file = ".env"


def get_settings(session: uuid4= None):
    return APPSettings()
