from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from src.domain.models.chat import Chat
from src.domain.models.message import Message
from src.domain.models.user import User


class IRepository(ABC):

    @abstractmethod
    async def get(self, *ids: int): ...

    @abstractmethod
    async def list(self, *kwargs): ...

    @abstractmethod
    async def create(self, **kwargs): ...

    @abstractmethod
    async def update(self, **kwargs): ...

    @abstractmethod
    async def delete(self, **kwargs): ...


class IChatRepository(IRepository, ABC):
    @abstractmethod
    async def create(self, chat: Chat) -> Chat: ...

class IUserRepository(IRepository, ABC):
    @abstractmethod
    async def create(self, user: User) -> User: ...

class IMessageRepository(IRepository, ABC):
    @abstractmethod
    async def create(self, message: Message) -> Message: ...

    async def get_by_idempotency_key(self, sender_id: int, key: UUID) -> Message: ...

    @abstractmethod
    async def list(self, chat_id: int, limit: int, offset: int) -> list[Message]: ...

    async def update(self, message_id: int, **kwargs) -> List[Message]: ...


class IGroupRepository(IRepository, ABC):
    @abstractmethod
    async def create(self, chat: Chat, creator: User): ...
