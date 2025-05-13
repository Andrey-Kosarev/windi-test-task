from src.domain.models.user import User
from src.domain.models.chat import Chat
from src.ports.repositories.abc import IChatRepository


class ChatService:
    def __init__(self, repository: IChatRepository, user: User):
        self.repository: IChatRepository = repository
        self.user: User = user

    async def create_chat(self, name: str, participants: list[User]) -> Chat:
        return await self.repository.create(name, participants)

    async def get_chat(self, id_: int) -> Chat:
        return await self.repository.get(id_)

    async def list_chats(self, limit: int, offset: int) -> list[Chat]:
        return await self.repository.list(limit, offset)

    async def delete_chat(self, chat_id: int):
        return await self.repository.delete(chat_id)

