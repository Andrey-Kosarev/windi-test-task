from fastapi import APIRouter
from src.entrypoints.webapp.routers.rest.v1.api_v1 import api_v1_router


rest_router = APIRouter()
rest_router.include_router(api_v1_router, prefix="/v1")