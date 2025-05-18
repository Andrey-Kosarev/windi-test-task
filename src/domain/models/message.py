from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import Optional
import json
from uuid import UUID

@dataclass
class Message:
    idempotency_key: UUID
    text: str
    sender_id: int
    chat_id: int
    id: Optional[int] = None
    timestamp: datetime =  field(default_factory=datetime.now)
    is_read: bool = False

    def to_json(self) -> str:
        return json.dumps(asdict(self), default=str)