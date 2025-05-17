from src.domain.models.user import User
from src.ports.repositories.abc import IUserRepository
from hashlib import md5


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository: IUserRepository = user_repository

    async def create_user(self, name: str, email: str, password: str) -> User:
        new_user: User = User(
            name=name,
            email=email,
            password=md5(password.encode()).hexdigest() # TODO: replace with injected hasher
        )

        created_user = await self.user_repository.create(new_user)
        return created_user

    async def get_user(self, user_id) -> User:
        users =  await self.user_repository.get(user_id)
        return users[0]