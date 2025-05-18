from pydantic import BaseModel
from uuid import UUID

class MessagePayload(BaseModel):
    chat_id: int
    text: str
    idempotency_key: UUID

class ReadMessagePayload(BaseModel):
    chat_id: int
    message_id: int

