from datetime import datetime, timezone

from src.domain.models.user import User


class Message:
    def __init__(self, text: str, sender: User):
        self.text: str = text
        self.sender: User = sender
        self.timestamp = datetime.now()
        self.read_by: list[User] = []

    