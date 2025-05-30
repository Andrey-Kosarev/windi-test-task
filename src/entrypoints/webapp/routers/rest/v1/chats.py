from typing import Annotated

from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.entrypoints.webapp.dependencies.database import get_db_session
from src.entrypoints.webapp.dependencies.services import ServiceFactory
from src.entrypoints.webapp.models.chat import CreateChatModel, ChatModel
from src.entrypoints.webapp.models.pagination import Pagination

chat_router = APIRouter()

@chat_router.get("/", response_model=list[ChatModel])
async def list_chats(request: Request, db_session: AsyncSession = Depends(get_db_session)):
    service_factory = ServiceFactory(db_session, request)
    chat_service = await service_factory.get_chat_service()
    chat_list = await chat_service.list_chats(10, 0)
    return chat_list


@chat_router.get("/{chat_id}")
async def get_chat(chat_id: int,  request: Request,  db_session: AsyncSession = Depends(get_db_session)):
    service_factory = ServiceFactory(db_session, request)
    chat_service = await service_factory.get_chat_service()
    chat = await chat_service.get_chat(chat_id)
    return chat

@chat_router.get("/{chat_id}/history")
async def get_chat(chat_id: int, p: Annotated[Pagination, Query()], request: Request, db_session: AsyncSession = Depends(get_db_session)):
    service_factory = ServiceFactory(db_session, request)
    chat_service = await service_factory.get_chat_service()
    chat = await chat_service.get_history(chat_id, p.limit, p.offset)
    return chat



@chat_router.post("/", response_model=ChatModel)
async def create_chat(chat: CreateChatModel, request: Request, db_session: AsyncSession = Depends(get_db_session)):
    service_factory = ServiceFactory(db_session, request)
    chat_service = await service_factory.get_chat_service()
    chat = await chat_service.create_chat(chat)
    return chat


@chat_router.delete("/{chat_id}")
async def list_chats(chat_id: int, request: Request, db_session: AsyncSession = Depends(get_db_session)):
    service_factory = ServiceFactory(db_session, request)
    chat_service = await service_factory.get_chat_service()
    await chat_service.delete_chat(chat_id)
    return
