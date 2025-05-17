from sqlalchemy.ext.asyncio.session import AsyncSession

from src.domain.models.message import Message
from src.ports.repositories.abc import IMessageRepository
from src.persistence.postgres.schema.messages import Messages

from sqlalchemy import insert, select, desc


class MessagePostgresRepository(IMessageRepository):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get(self, *ids: int):
        pass

    async def list(self, chat_id:int,  limit: int, offset: int) -> list[Message]:
        query = select(Messages)\
            .where(Messages.chat_id == chat_id)\
            .limit(limit).offset(offset)\
            .order_by(desc(Messages.timestamp))

        message_records = (await self.session.execute(query)).fetchall()

        return [
            Message(
                id=msg.id,
                text=msg.text,
                sender_id=msg.sender_id,
                chat_id=msg.chat_id
            ) for (msg, ) in message_records
        ]



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