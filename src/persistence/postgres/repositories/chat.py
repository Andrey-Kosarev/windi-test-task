from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from src.domain.models.chat import Chat
from src.domain.models.user import User
from src.ports.repositories.abc import IChatRepository
from src.persistence.postgres.schema.chats import Chats, ChatParticipants


class ChatPostgresRepository(IChatRepository):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    def _parse_chat_from_dict(self, chat: dict):
        ...

    async def get(self, *ids: int): ...

    async def list(self, limit: int, offset: int): ...

    async def create(self, name: str, participants: List[User]) -> Chat:
        store_chat_query = insert(Chats).values({Chats.name: name}).returning(Chats)

        new_chat_record = await self.session.execute(store_chat_query)
        new_chat = new_chat_record.mappings().fetchone()
        new_chat = new_chat.get("Chats")

        store_participants_query = insert(ChatParticipants).values([
            {ChatParticipants.user_id: user_id, ChatParticipants.chat_id: new_chat.id} for user_id in participants
        ])

        await self.session.execute(store_participants_query)
        return Chat(id=new_chat.id, name=new_chat.name, participants=participants)


    async def update(self, id_: int, **kwargs): ...

    async def delete(self, id_: int): ...
