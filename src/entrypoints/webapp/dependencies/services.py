from fastapi import Request

from src.domain.models.user import User
from src.domain.services.chat_service import ChatService
from src.domain.services.user_service import UserService
from src.persistence.postgres.repositories.chat import ChatPostgresRepository
from sqlalchemy.ext.asyncio import AsyncSession

from src.persistence.postgres.repositories.group import GroupPostgresRepository
from src.persistence.postgres.repositories.message import MessagePostgresRepository
from src.persistence.postgres.repositories.user import UserPostgresRepository


class ServiceFactory:

    def __init__(self, db_session: AsyncSession, request: Request):
        self.db_session = db_session
        self.request = request

    async def _get_user(self):
        user_id = self.request.scope["user_id"]
        user_repository = UserPostgresRepository(self.db_session)
        user_service = UserService(user_repository)
        return await user_service.get_user(user_id)


    async def get_chat_service(self):
        user = await self._get_user()
        chat_repository = ChatPostgresRepository(self.db_session)
        user_repository = UserPostgresRepository(self.db_session)
        message_repository = MessagePostgresRepository(self.db_session)
        group_repository = GroupPostgresRepository(self.db_session)

        return ChatService(user, chat_repository, user_repository, message_repository, group_repository)

    def get_user_service(self):
        user_repository = UserPostgresRepository(self.db_session)
        return UserService(user_repository)
