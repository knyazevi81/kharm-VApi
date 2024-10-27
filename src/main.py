from fastapi import FastAPI
from fastapi.responses import FileResponse
from src.baseapi import BaseReq

from src.users.router import router as users_router

app = FastAPI(
    title="SaveBit API service",
    docs_url="/docs",
    redoc_url=None
)

app.include_router(users_router)

@app.get("/")
async def get_main():
    return {
        "detail": "Дружочек, ты куда лезешь?)"
    }
