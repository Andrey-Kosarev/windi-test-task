from fastapi import FastAPI
from src.entrypoints.webapp.routers.rest.rest_router import rest_router
from src.entrypoints.webapp.routers.ws.chats import ws_router
from src.entrypoints.webapp.middlewares.auth import TrustAuthMiddleware


app = FastAPI()
app.add_middleware(TrustAuthMiddleware)

app.include_router(rest_router, prefix="/rest")
app.include_router(ws_router, prefix="/ws")