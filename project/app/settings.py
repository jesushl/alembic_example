from pydantic import BaseSettings
from functools import lru_cache
# constants from environment
from app.constants import DATABASE_URL

class APPSettings(BaseSettings):
    app_name: str = "Companies"
    admin_email: str = "jesushledon@gmail.com"
    sqlalchemy_database_url: str = DATABASE_URL
    alphavantage_key: str
    

    class Config:
        env_file = "app/.env"


@lru_cache()
def get_settings():
    return APPSettings()