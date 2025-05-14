from pydantic import BaseModel

class CreateChatModel(BaseModel):
    name: str
    participants: list[int]

class ChatModel(CreateChatModel):
    id: int