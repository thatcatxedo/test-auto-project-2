from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Your API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "FastAPI project created with automated setup script"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]  # Frontend URL

    class Config:
        env_file = ".env"

settings = Settings()
