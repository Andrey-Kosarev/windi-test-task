from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.models.user import User
from src.entrypoints.webapp.dependencies.database import get_db_session
from src.entrypoints.webapp.dependencies.services import get_chat_service
from src.entrypoints.webapp.models.chat import CreateChatModel

chat_router = APIRouter()

@chat_router.get("/")
async def list_chats(db_session: AsyncSession = Depends(get_db_session)):
    chat_service = get_chat_service(db_session)
    chat_list = await chat_service.list_chats(10, 0)
    return chat_list


@chat_router.get("/{chat_id}")
async def get_chat(chat_id: int,  db_session: AsyncSession = Depends(get_db_session)):
    chat_service = get_chat_service(db_session)
    chat = await chat_service.get_chat(chat_id)
    return chat


@chat_router.post("/")
async def create_chat(chat: CreateChatModel, db_session: AsyncSession = Depends(get_db_session)):
    chat_service = get_chat_service(db_session)
    chat = await chat_service.create_chat(chat.name, chat.participants)
    return chat


@chat_router.delete("/{chat_id}")
async def list_chats(chat_id: int,  db_session: AsyncSession = Depends(get_db_session)):
    chat_service = get_chat_service(db_session)
    await chat_service.delete_chat(chat_id)
    return
