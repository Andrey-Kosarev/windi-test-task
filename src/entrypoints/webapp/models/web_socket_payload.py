from pydantic import BaseModel
from typing import Literal

class WebSocketPayload(BaseModel):
    method: str
    payload: dict


class WebSocketResponsePayload(BaseModel):
    method: str
    status: Literal["success", "fail"]
    payload: dict