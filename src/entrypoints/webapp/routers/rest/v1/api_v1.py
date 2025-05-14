from fastapi import APIRouter
from src.entrypoints.webapp.routers.rest.v1.chats import chat_router
from src.entrypoints.webapp.routers.rest.v1.users import user_router

api_v1_router = APIRouter()
api_v1_router.include_router(chat_router, prefix="/chats")
api_v1_router.include_router(user_router, prefix="/users")
