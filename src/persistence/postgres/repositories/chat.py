from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.domain.models.chat import Chat
from src.persistence.postgres.schema import Users
from src.ports.repositories.abc import IChatRepository
from src.persistence.postgres.schema.chats import Chats, ChatParticipants


class ChatPostgresRepository(IChatRepository):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    def _parse_chat_from_dict(self, chat: dict):
        ...

    async def get(self, *ids: int) -> list[Chat]:
        chat_list_query = select(Chats).where(Chats.id.in_(ids))
        chats_response = await self.session.execute(chat_list_query)

        chats: dict[int: Chat] = {}
        for (db_chat, ) in chats_response.fetchall():
            chats[db_chat.id] = Chat(id=db_chat.id, name=db_chat.name, participants=[], type=db_chat.type)

        participants_list_query = select(Users, ChatParticipants.chat_id)\
            .join(ChatParticipants, onclause=(Users.id == ChatParticipants.user_id))\
            .where(ChatParticipants.chat_id.in_(chats.keys()))

        participants_response = await self.session.execute(participants_list_query)

        for user, chat_id in participants_response.fetchall():
            chats[chat_id].participants.append(user)

        return list(chats.values())


    async def list(self, limit: int, offset: int) -> list[Chat]:
        chat_list_query = select(Chats).limit(limit).offset(offset)
        chats_response = await self.session.execute(chat_list_query)

        chats: dict[int: Chat] = {}
        for (db_chat, ) in chats_response.fetchall():
            chats[db_chat.id] = Chat(id=db_chat.id, name=db_chat.name, participants=[])

        participants_list_query = select(Users, ChatParticipants.chat_id)\
            .join(ChatParticipants, onclause=(Users.id == ChatParticipants.user_id))\
            .where(ChatParticipants.chat_id.in_(chats.keys()))

        participants_response = await self.session.execute(participants_list_query)

        for user, chat_id in participants_response.fetchall():
            chats[chat_id].participants.append(user)

        return list(chats.values())

    async def create(self, chat: Chat) -> Chat:
        store_chat_query = insert(Chats).values({
            Chats.name: chat.name,
            Chats.type: chat.type
        }).returning(Chats)

        new_chat_record = await self.session.execute(store_chat_query)
        new_chat = new_chat_record.mappings().fetchone()
        new_chat = new_chat.get("Chats")

        store_participants_query = insert(ChatParticipants).values([
            {ChatParticipants.user_id: user.id, ChatParticipants.chat_id: new_chat.id} for user in chat.participants
        ])

        await self.session.execute(store_participants_query)
        return Chat(id=new_chat.id, name=new_chat.name, participants=chat.participants, type=chat.type)


    async def update(self, id_: int, **kwargs): ...

    async def delete(self, id_: int): ...
