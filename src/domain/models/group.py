from dataclasses import dataclass
from src.domain.models.user import User

@dataclass
class Group:
    name: str
    creator: User
    id: int = None