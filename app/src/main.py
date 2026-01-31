import os
import redis.asyncio as redis
from contextlib import asynccontextmanager
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.src.routers import router
from app.src.services import redis_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    global redis_client
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    yield
    await redis_client.close()

app = FastAPI(lifespan=lifespan)
Instrumentator().instrument(app).expose(app)

app.include_router(router, prefix="/api/v1")