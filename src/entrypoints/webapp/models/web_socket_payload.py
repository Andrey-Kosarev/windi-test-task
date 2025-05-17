from pydantic import BaseModel

class WebSocketPayload(BaseModel):
    method: str
    payload: dict