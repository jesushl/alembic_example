from pydantic import BaseSettings
from functools import lru_cache

class APPSettings(BaseSettings):
    app_name: str = "Companies"
    admin_email: str = "jesushledon@gmail.com"
    alphavantage_key: str
    class Config:
        env_file = "app/.env"


@lru_cache()
def get_settings():
    return APPSettings()