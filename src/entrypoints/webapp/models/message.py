from pydantic import BaseModel

class MessagePayload(BaseModel):
    chat_id: int
    text: str
