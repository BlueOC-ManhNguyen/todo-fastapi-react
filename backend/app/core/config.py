from pydantic_settings import BaseSettings
from pydantic import validator
from pydantic import PostgresDsn


class Settings(BaseSettings):
    SECRET_KEY: str = "123"
    API_PREFIX: str = ""
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM: str = "HS256"

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_SERVER: str = "postgresql+psycopg2"
    POSTGRES_DB: str = "postgres"
    DATABASE_URI: str = ""
    POSTGRES_CONNECTION_POOL_SIZE: int = 20

    # @validator('DATABASE_URI', pre=True)
    # def assemble_db_connection(cls, v, values):
    #     if isinstance(v, str):
    #         return v
    #     return PostgresDsn.build(
    #         scheme='postgresql',
    #         username=values.get('POSTGRES_USER'),
    #         password=values.get('POSTGRES_PASSWORD'),
    #         host=values.get('POSTGRES_SERVER'),
    #         path=f"{values.get('POSTGRES_DB') or ''}",
    #     )
    class Config:
        env_file = ".env"


settings = Settings()
