from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.entrypoints.webapp.dependencies.database import get_db_session
from src.entrypoints.webapp.dependencies.services import ServiceFactory
from src.entrypoints.webapp.models.user import CreateUserModel, UserModel

user_router = APIRouter()


@user_router.post("/", response_model=UserModel)
async def create_user(user: CreateUserModel, request: Request, db_session: AsyncSession = Depends(get_db_session)):
    service_factory = ServiceFactory(db_session, request)
    service = service_factory.get_user_service()
    created_user = await service.create_user(user.name, user.email, user.password)
    return created_user