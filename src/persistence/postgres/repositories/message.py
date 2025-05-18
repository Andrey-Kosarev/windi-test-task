from typing import List
from uuid import UUID
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.domain.exceptions.validation import InvalidChatType, DuplicateIdempotencyKey
from src.domain.models.message import Message
from src.ports.repositories.abc import IMessageRepository
from src.persistence.postgres.schema.messages import Messages

from sqlalchemy import select, update, desc
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError


class MessagePostgresRepository(IMessageRepository):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get(self, *ids: int):
        pass

    async def get_by_idempotency_key(self, sender_id: int, key: UUID) -> Message:
        query = select(Messages).where(
                Messages.sender_id == sender_id,
                Messages.idempotency_key == key
            ).limit(1)

        message_records = (await self.session.execute(query)).fetchone()

        return [
            Message(
                id=msg.id,
                text=msg.text,
                sender_id=msg.sender_id,
                chat_id=msg.chat_id,
                is_read=msg.is_read,
                idempotency_key=msg.idempotency_key
            ) for (msg,) in message_records
        ]


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
                chat_id=msg.chat_id,
                is_read=msg.is_read
            ) for (msg, ) in message_records
        ]

    async def create(self, message: Message) -> Message:
        insert_stmt = insert(Messages).values({
            Messages.chat_id: message.chat_id,
            Messages.text: message.text,
            Messages.sender_id: message.sender_id,
            Messages.timestamp: message.timestamp,
            Messages.is_read: message.is_read,
            Messages.idempotency_key: message.idempotency_key
        }).returning(Messages)

        insert_stmt = insert_stmt.on_conflict_do_update(
            index_elements=[Messages.idempotency_key],
            set_={
                Messages.idempotency_key: insert_stmt.excluded.idempotency_key
            }
        )

        response = await self.session.execute(insert_stmt)
        data = response.fetchone()[0]

        new_message = Message(
            id=data.id,
            text=data.text,
            sender_id=data.sender_id,
            timestamp=data.timestamp,
            is_read=data.is_read,
            chat_id=data.chat_id,
            idempotency_key=data.idempotency_key
        )

        return new_message


    async def update(self, message_id: int, **kwargs) -> List[Message]:
        query = update(Messages).values(kwargs).where(Messages.id == message_id).returning(Messages)
        db_response  = await self.session.execute(query)

        updated_messages = list()
        for (returned_message, ) in db_response.fetchall():
            updated_messages.append(
                Message(
                    id=returned_message.id,
                    text=returned_message.text,
                    sender_id=returned_message.sender_id,
                    timestamp=returned_message.timestamp,
                    is_read=returned_message.is_read,
                    chat_id=returned_message.chat_id,
                    idempotency_key=returned_message.idempotency_key
                )
            )

        return updated_messages

    async def delete(self, id_: int):
        pass