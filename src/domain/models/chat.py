from dataclasses import dataclass
from typing import Optional
from src.domain.models.user import User


@dataclass
class Chat:
    name: str
    type: str
    participants: list[User]
    id: Optional[int] = None
