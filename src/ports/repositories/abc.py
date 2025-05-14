from abc import ABC, abstractmethod
from typing import Optional

from src.domain.models.chat import Chat
from src.domain.models.user import User


class IRepository(ABC):

    @abstractmethod
    async def get(self, *ids: int): ...

    @abstractmethod
    async def list(self, limit: int, offset: int): ...

    @abstractmethod
    async def create(self, **kwargs): ...

    @abstractmethod
    async def update(self, id_: int, **kwargs): ...

    @abstractmethod
    async def delete(self, id_: int): ...


class IChatRepository(IRepository, ABC):
    @abstractmethod
    async def create(self, name: str, participants: list[User]) -> Chat: ...

class IUserRepository(IRepository, ABC):
    @abstractmethod
    async def create(self, user: User) -> User: ...

class IMessageRepository(IRepository, ABC): ...
class IGroupRepository(IRepository, ABC): ...