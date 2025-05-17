from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from src.domain.models.chat import Chat
from src.domain.models.group import Group
from src.domain.models.user import User
from src.ports.repositories.abc import IGroupRepository
from src.persistence.postgres.schema.groups import Groups

class GroupPostgresRepository(IGroupRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, chat: Chat, creator: User) -> Group:
        query = insert(Groups).values({
            Groups.name: chat.name,
            Groups.created_by: creator.id,
            Groups.chat_id: chat.id
        }).returning(Groups)

        db_group =  (await self.session.execute(query)).fetchone()[0]

        new_group = Group(
            id=db_group.id,
            name=db_group.name,
            creator=creator
        )

        return new_group


    async def get(self, *ids: int):
        pass

    async def list(self, *kwargs):
        pass

    async def update(self, **kwargs):
        pass

    async def delete(self, **kwargs):
        pass