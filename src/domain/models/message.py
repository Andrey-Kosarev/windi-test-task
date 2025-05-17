from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Optional

from src.domain.models.user import User

@dataclass
class Message:
    text: str
    sender_id: int
    chat_id: int
    id: Optional[int] = None
    timestamp: datetime = datetime.now()
    is_read: bool = False