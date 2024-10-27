from fastapi import APIRouter

app = APIRouter(
    prefix="/payload",
    tags=["Сервис оплат"]
)
