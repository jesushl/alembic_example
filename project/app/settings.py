from pydantic import BaseSettings
from functools import lru_cache

# constants from environment
from app.constants import get_database_url


class APPSettings(BaseSettings):
    app_name: str = "Companies"
    admin_email: str = "jesushledon@gmail.com"
    database_url: str = get_database_url()
    alphavantage_key: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return APPSettings()
