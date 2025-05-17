from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.exceptions.access import ChatAccessError
from src.entrypoints.webapp.dependencies.database import get_db_session
from src.entrypoints.webapp.dependencies.services import ServiceFactory
from src.entrypoints.webapp.managers.chat_connection_manager import connection_manager
from src.entrypoints.webapp.managers.chat_method_handlers.send_message_handler import SendMessageHandler
from src.entrypoints.webapp.models.web_socket_payload import WebSocketPayload

ws_router = APIRouter()

handlers = {
    "send_message": SendMessageHandler,
}


@ws_router.websocket("/")
async def handle_chats(ws: WebSocket, db_session: AsyncSession = Depends(get_db_session)):
    user_id = ws.scope["user_id"]
    await connection_manager.connect(user_id, ws)
    service_factory = ServiceFactory(db_session, ws)
    chat_service = await service_factory.get_chat_service()
    while True:
        raw_msg = await ws.receive_text()
        try:
            message = WebSocketPayload.model_validate_json(raw_msg)
            handler = handlers.get(message.method, None)
            if handler is None:
                await ws.send_text(f"Invalid method : {message.method}" )
                continue

            await handler.handle(chat_service, user_id, message.payload)
            await db_session.commit()
        except ChatAccessError:
            await connection_manager.send_message(user_id, {"error": "access denied"})

        except Exception as exc:
            raise exc
            #await ws.send_text("Invalid data")