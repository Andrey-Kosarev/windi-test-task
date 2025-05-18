import json

from src.domain.models.message import Message
from src.domain.services.chat_service import ChatService
from src.entrypoints.webapp.managers.chat_connection_manager import connection_manager
from src.entrypoints.webapp.managers.chat_method_handlers.abc import IWSHandler
from src.entrypoints.webapp.models.message import ReadMessagePayload
from src.entrypoints.webapp.models.web_socket_payload import WebSocketResponsePayload


class ReadMessageHandler(IWSHandler):
    @staticmethod
    async def handle(chat_service: ChatService, user_id: int, payload: dict) -> str:
        read_message = ReadMessagePayload(**payload)
        chat = await chat_service.get_chat(read_message.chat_id)
        new_messages: list[Message] =  await chat_service.read_message(chat, message_id=read_message.message_id)
        await connection_manager.send_message(
            user_id,
            json.dumps([m.to_json() for m in new_messages])
        )

        return WebSocketResponsePayload(
            method="read_message",
            status="success",
            payload={
                "data": new_messages
            }
        ).model_dump_json()
