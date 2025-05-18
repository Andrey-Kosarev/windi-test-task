from pydantic import BaseModel

class MessagePayload(BaseModel):
    chat_id: int
    text: str

class ReadMessagePayload(BaseModel):
    chat_id: int
    message_id: int

