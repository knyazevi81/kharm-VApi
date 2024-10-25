from fastapi import APIRouter

from src.users.schemas import IntegAuth
from src.config import settings

from src.users.baseusers import UserReq

router = APIRouter(
    prefix="/users",
    tags=["Эндпоинт для работы с юзерами"] 
)

@router.post("/all_users")
async def get_all_users(data: IntegAuth):
    if data.integration_token == settings.integration_token:
        return UserReq.get_list_users()
