from src.domain.models.user import User
from src.domain.models.message import Message


class Chat:
    def __init__(self, name: str, admin: User, participants: list[User]):
        self.name:str = name
        self.participants: list[User] = participants
        self.admins: list[User]

    def send_message(self, message: Message):
        ...

    def add_user(self, user: User):
        self.participants.app
