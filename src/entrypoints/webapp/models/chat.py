from pydantic import BaseModel

from src.entrypoints.webapp.models.user import UserModel

class ChatBaseModel(BaseModel):
    name: str

class CreateChatModel(ChatBaseModel):
    participants: list[int]

class ChatModel(ChatBaseModel):
    id: int
    participants: list[UserModel]