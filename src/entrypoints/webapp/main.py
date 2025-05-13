from fastapi import FastAPI
from src.entrypoints.webapp.routers.rest.rest_router import rest_router
app = FastAPI()
app.include_router(rest_router, prefix="/rest")
#app.include_router("/ws")