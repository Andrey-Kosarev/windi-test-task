import asyncio
from typing import Optional
from fastapi import WebSocket
from fastapi.websockets import WebSocketState

from src.domain.models.chat import Chat


class ChatConnectionManagerInMemory:
    def __init__(self):
        self.connections: dict[int, WebSocket] = dict()

    def _get_connection(self, user_id: int) -> Optional[WebSocket]:
        user_connection = self.connections.get(user_id, None)
        if user_connection is None:
            return None

        if user_connection.client_state == WebSocketState.DISCONNECTED:
            self.connections.pop(user_id)
            return None

        return user_connection

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.connections[user_id] = websocket
        return True

    async def send_message(self, user_id: int, message: str):
        user_connection = self._get_connection(user_id)
        if user_connection:
            await user_connection.send_bytes(message)

    async def disconnect(self, user_id: int):
        ws = self.connections.pop(user_id)
        await ws.close()

    async def notify_chat(self, chat: Chat, message: str):
        await asyncio.gather(*(
             self.send_message(user.id, message) for user in chat.participants
        ))


connection_manager = ChatConnectionManagerInMemory()