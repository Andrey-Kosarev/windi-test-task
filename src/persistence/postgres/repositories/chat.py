from sqlalchemy.ext.asyncio import AsyncSession
from src.ports.repositories.abc import IChatRepository


class ChatPostgresRepository(IChatRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id_: int): ...

    async def list(self, limit: int, offset: int): ...

    async def create(self, **kwargs): ...

    async def update(self, id_: int, **kwargs): ...

    async def delete(self, id_: int): ...
