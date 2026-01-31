from fastapi import APIRouter
from app.src.models import AntifraudRequest, AntifraudResponse
from app.src.services import check_antifraud

router = APIRouter()
async def perform_antifraud_check(request: AntifraudRequest):
    return await check_antifraud(request)