from fastapi import APIRouter

router = APIRouter(
    prefix="/vpn",
    tags=["Сервис для работы с ВПН"]
)


@router.post("/create_vpn")
async def create_vpn():
    pass