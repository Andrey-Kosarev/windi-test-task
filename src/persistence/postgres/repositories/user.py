from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.models.user import User
from src.persistence.postgres.schema.users import Users
from src.ports.repositories.abc import IUserRepository


class UserPostgresRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get(self, *ids: int) -> list[User]:
        user_query = select(Users).where(Users.id.in_(ids))
        users_response = await self.session.execute(user_query)

        for user_data in users_response.mappings().fetchall():
            print(user_data)

        return [User(id=userid, name="myname", email="e@mail.com", password="hashed") for userid in ids]


    def list(self, limit: int, offset: int):
        pass

    async def create(self, user: User) -> User:
        insert_query = insert(Users).values({
            Users.name: user.name,
            Users.email: user.email,
            Users.password: user.password
        }).returning(Users)

        new_user_record = await self.session.execute(insert_query)
        new_user: Users = new_user_record.mappings().fetchone().get("Users")

        return User(id=new_user.id, name=new_user.name, email=new_user.email, password=new_user.password)

    def update(self, id_: int, **kwargs):
        pass

    def delete(self, id_: int):
        pass