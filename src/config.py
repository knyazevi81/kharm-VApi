from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    login: str
    password: str
    base_url: str
    integration_token: str

    class Config:
        env_file = ".env"

settings = Settings()