from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional

from src.domain.models.user import User

@dataclass
class Message:
    text: str
    sender_id: int
    chat_id: int
    id: Optional[int] = None
    timestamp: datetime =  field(default_factory=datetime.now)
    is_read: bool = False