from abc import ABC, abstractmethod

from src.domain.services.chat_service import ChatService


class IWSHandler(ABC):

    @staticmethod
    @abstractmethod
    async def handle(chat_service: ChatService, user_id: int, message_payload: dict) -> str: ...