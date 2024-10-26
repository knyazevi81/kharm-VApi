from fastapi import APIRouter, HTTPException, status
import json

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
    
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Брат, ты не авторизован"
    )

@router.post("")
async def get_user(user_id: str, data: IntegAuth):
    if data.integration_token == settings.integration_token:
        response = UserReq.get_user_info(user_id)
        return response
    
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Брат, ты не авторизован"
    )

@router.post("/online_users")
async def get_online_users(data: IntegAuth):
    if data.integration_token == settings.integration_token:
        response = UserReq.onlines()
        return response
    
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Брат, ты не авторизован"
    )


@router.post("/get_connection")
async def get_all_users(user_id: str, connection_id: int, data: IntegAuth):
    if data.integration_token == settings.integration_token:
        response = UserReq.get_user_info(user_id)
        
        if len(response["clientStats"]) < connection_id-1 or connection_id < 0:
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Брат, неверно указан айдишник подключения"
            )

        client_settings = json.loads(response["settings"])
        client_stream_settings = json.loads(response["streamSettings"])

        connection_key = [
            f"{response['protocol']}://",
            f"{client_settings['clients'][connection_id]['id']}@",
            f"{settings.host}:{response['port']}?",
            f"type={client_stream_settings['network']}&",
            f"security={client_stream_settings['security']}#",
            f"{response['remark']}-{response['clientStats'][connection_id]['email']}"
        ]

        return "".join(connection_key)
    
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Брат, ты не авторизован"
    )

