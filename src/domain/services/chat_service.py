from typing import Optional

from src.domain.exceptions.access import ChatAccessError
from src.domain.exceptions.validation import InvalidChatType, InvalidNumberOfParticipants
from src.domain.models.message import Message
from src.domain.models.user import User
from src.domain.models.chat import Chat
from src.ports.repositories.abc import IChatRepository, IUserRepository, IMessageRepository, IGroupRepository


class ChatService:
    _allowed_chat_types = ("private", "group")

    def __init__(
            self,
            chat_repository: IChatRepository,
            user_repository: IUserRepository,
            message_repository: IMessageRepository,
            group_repository: IGroupRepository
    ):
        self.chat_repository: IChatRepository = chat_repository
        self.user_repository: IUserRepository = user_repository
        self.message_repository: IMessageRepository = message_repository
        self.group_repository: IGroupRepository = group_repository

    async def create_chat(self, chat: Chat) -> Chat:
        if chat.type not in self._allowed_chat_types:
            raise InvalidChatType()

        if chat.type == "private" and len(chat.participants) > 2:
            raise InvalidNumberOfParticipants()

        chat.participants = await self.user_repository.get(*chat.participants)

        chat = await self.chat_repository.create(chat)

        if chat.type == "group":
            await self.group_repository.create(chat,  User(id=1, name="a", email="", password="") )

        return chat

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

