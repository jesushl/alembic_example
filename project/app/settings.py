from pydantic import BaseSettings
from functools import lru_cache

# constants from environment
from app.constants import DATABASE_URL


class APPSettings(BaseSettings):
    app_name: str = "Companies"
    admin_email: str = "jesushledon@gmail.com"
    database_url: str = DATABASE_URL
    alphavantage_key: str


def get_settings():
    return APPSettings()
