from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

class TrustAuthMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def _raise_error_http(self,  code: int, scope, receive, send):
        response = JSONResponse(
            {"detail": "Unauthorized"},
            status_code=code,
        )
        await response(scope, receive, send)
        return

    async def _raise_error_ws(self, code: int, send):
        await send({
            "type": "websocket.close",
            "code": 1008,  # Policy violation
        })
        return

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        raw_headers = scope.get("headers", [])

        headers = {k.decode(): v.decode() for k, v in raw_headers}
        user_id = headers.get("user_id", None)

        if user_id is None:
            if scope["type"] == "http":
                await self._raise_error_http(401, scope, receive, send)
                return
            if scope["type"] == "websocket":
                await self._raise_error_ws(1008, send)
                return

        scope["user_id"] = user_id
        await self.app(scope, receive, send)