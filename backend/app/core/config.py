from pydantic_settings import BaseSettings
from pydantic import validator
from pydantic import PostgresDsn


class Settings(BaseSettings):
    SECRET_KEY: str = "123"
    API_PREFIX: str = ""
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM: str = "HS256"

    DATABASE_URI: str
    POSTGRES_CONNECTION_POOL_SIZE: int = 20

    class Config:
        env_file = ".env"


settings = Settings()
