from fastapi import FastAPI

from app.api.v1 import api_router as api_v1_router
from app.core.configuration import settings


app = FastAPI()

app.include_router(api_v1_router, prefix=settings.API_V1_STR)
