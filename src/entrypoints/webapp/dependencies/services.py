from src.domain.services.chat_service import ChatService
from src.domain.services.user_service import UserService
from src.persistence.postgres.repositories.chat import ChatPostgresRepository
from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.postgres.repositories.group import GroupPostgresRepository
from src.persistence.postgres.repositories.message import MessagePostgresRepository
from src.persistence.postgres.repositories.user import UserPostgresRepository


def get_chat_service(session: AsyncSession) -> ChatService:
    chat_repository = ChatPostgresRepository(session)
    user_repository = UserPostgresRepository(session)
    message_repository = MessagePostgresRepository(session)
    group_repository = GroupPostgresRepository(session)

    return ChatService(chat_repository, user_repository, message_repository, group_repository)

def get_user_service(session: AsyncSession):
    user_repository = UserPostgresRepository(session)
    return UserService(user_repository)