from typing import Optional

from src.domain.exceptions.access import ChatAccessError
from src.domain.models.message import Message
from src.domain.models.user import User
from src.domain.models.chat import Chat
from src.ports.repositories.abc import IChatRepository, IUserRepository, IMessageRepository


class ChatService:
    def __init__(
            self,
            chat_repository: IChatRepository,
            user_repository: IUserRepository,
            message_repository: IMessageRepository
    ):
        self.chat_repository: IChatRepository = chat_repository
        self.user_repository: IUserRepository = user_repository
        self.message_repository: IMessageRepository = message_repository

    async def create_chat(self, name: str, participant_ids: list[int]) -> Chat:
        users = await self.user_repository.get(*participant_ids)
        return await self.chat_repository.create(name, users)

    async def get_chat(self, chat_id: int) -> Chat:
        chat = await self.chat_repository.get(chat_id)
        return chat[0]

    async def check_access(self, user_id: int, chat_id: int) -> Optional[Chat]:
        chat = await self.chat_repository.get(chat_id)

        if user_id not in (p.id for p in chat[0].participants):
            return None
        return chat

    async def get_history(self, chat_id: int, limit: int, offset: int):
        return await self.message_repository.list(chat_id=chat_id, limit=limit, offset=offset)

    async def store_message(self, chat: Chat, message: Message):
        chat = await self.check_access(message.sender_id, chat_id=chat.id)
        if chat is None:
            raise ChatAccessError()

        await self.message_repository.create(message)

    async def list_chats(self, limit: int, offset: int) -> list[Chat]:
        return await self.chat_repository.list(limit, offset)

    async def delete_chat(self, chat_id: int):
        return await self.chat_repository.delete(chat_id)

