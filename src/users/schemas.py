from pydantic import BaseModel

class IntegAuth(BaseModel):
    """Схема для проверки интеграционного токена"""
    integration_token: str

    class Config:
        orm_mode = True