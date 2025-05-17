from src.domain.models.message import Message
from src.domain.services.chat_service import ChatService
from src.entrypoints.webapp.managers.chat_connection_manager import connection_manager
from src.entrypoints.webapp.models.message import MessagePayload


class SendMessageHandler:
    @staticmethod
    async def handle(chat_service: ChatService, user_id: int, message_payload: dict) -> str:
        message = MessagePayload(**message_payload)

        message_object = Message(
            text=message.text,
            sender_id=user_id,
            chat_id=message.chat_id
        )

        chat = await chat_service.get_chat(message.chat_id)
        stored_message = await chat_service.store_message(chat, message_object)
        await connection_manager.notify_chat(chat, stored_message.to_json())

        return "message_sent_successfully"

