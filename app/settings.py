from pydantic import BaseSettings


class APPSettings(BaseSettings):
    app_name: str = "Companies"
    admin_email: str = "jesushledon@gmail.com"

    class Config:
        env_file = ".env"