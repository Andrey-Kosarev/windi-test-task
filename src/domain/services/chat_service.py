from src.domain.models.user import User
from src.domain.models.chat import Chat
from src.ports.repositories.abc import IChatRepository, IUserRepository


class ChatService:
    def __init__(self, chat_repository: IChatRepository, user_repository: IUserRepository, user: User):
        self.chat_repository: IChatRepository = chat_repository
        self.user_repository: IUserRepository = user_repository
        self.user: User = user

    async def create_chat(self, name: str, participant_ids: list[int]) -> Chat:
        users = await self.user_repository.get(*participant_ids)

        if self.user not in users:
            users.append(self.user)

        return await self.chat_repository.create(name, users)

    async def get_chat(self, id_: int) -> Chat:
        return await self.chat_repository.get(id_)

    async def list_chats(self, limit: int, offset: int) -> list[Chat]:
        return await self.chat_repository.list(limit, offset)

    async def delete_chat(self, chat_id: int):
        return await self.chat_repository.delete(chat_id)

