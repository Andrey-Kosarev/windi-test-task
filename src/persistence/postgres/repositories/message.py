from sqlalchemy.ext.asyncio.session import AsyncSession

from src.domain.models.message import Message
from src.ports.repositories.abc import IMessageRepository
from src.persistence.postgres.schema.messages import Messages

from sqlalchemy import insert


class MessagePostgresRepository(IMessageRepository):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get(self, *ids: int):
        pass

    async def list(self, limit: int, offset: int):
        pass

    async def create(self, message: Message) -> Message:
        insert_query = insert(Messages).values({
            Messages.chat_id: message.chat_id,
            Messages.text: message.text,
            Messages.sender_id: message.sender_id,
            Messages.timestamp: message.timestamp,
            Messages.is_read: message.is_read
        }).returning(Messages)

        response = await self.session.execute(insert_query)
        data = response.fetchone()[0]

        new_message = Message(
            id=data.id,
            text=data.text,
            sender_id=data.sender_id,
            timestamp=data.timestamp,
            is_read=data.is_read,
            chat_id=data.chat_id
        )

        return new_message


    async def update(self, id_: int, **kwargs):
        pass

    async def delete(self, id_: int):
        pass