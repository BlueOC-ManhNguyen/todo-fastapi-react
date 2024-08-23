from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = '123'
    API_PREFIX: str = ''
    DATABASE_URL: str = ''
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM: str = 'HS256'

    class Config:
        env_file = '.env'

settings = Settings()
