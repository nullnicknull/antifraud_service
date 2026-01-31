import json
from datetime import date
import redis.asyncio as redis
from app.models import AntifraudRequest, AntifraudResponse

redis_client: Optional[redis.Redis] = None

async def check_antifraud(data: AntifraudRequest) -> AntifraudResponse:
    cache_key = f"antifraud:{hash(json.dumps(data.dict(), sort_keys=True, default=str))}"

    if redis_client:
        cached_result = await redis_client.get(cache_key)
        if cached_result:
            return AntifraudResponse.parse_raw(cached_result)

    stop_factors = []
    if not data.phone_number.startswith("+7") and not data.phone_number.startswith("8"):
        stop_factors.append("Некорректный формат телефона (не начинается с +7 или 8)") 

    if (date.today().year - data.birth_date.year) < 18:
        stop_factors.append("Клиенту меньше 18 лет") 

    if any(not loan.is_closed for loan in data.loans_history):
        stop_factors.append("Есть незакрытый займ") 

    result = not bool(stop_factors)
    response = AntifraudResponse(stop_factors=stop_factors, result=result)

    if redis_client:
        await redis_client.setex(cache_key, 60, response.json())

    return response