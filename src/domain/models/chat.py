from dataclasses import dataclass
from typing import Optional
from src.domain.models.user import User


@dataclass(frozen=True)
class Chat:
    name:str
    participants: list[User]
    id: Optional[int] = None
