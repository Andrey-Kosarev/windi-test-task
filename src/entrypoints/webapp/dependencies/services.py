from src.domain.models.user import User
from src.domain.services.chat_service import ChatService
from src.persistence.postgres.repositories.chat import ChatPostgresRepository
from sqlalchemy.ext.asyncio import AsyncSession


def get_chat_service(session: AsyncSession) -> ChatService:
    chat_repository = ChatPostgresRepository(session)
    return ChatService(chat_repository, User("1"))