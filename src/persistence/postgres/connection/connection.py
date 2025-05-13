from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.config import ENV_CONFIG


ENGINE = create_async_engine(ENV_CONFIG.DB_URL)

AsyncSession = async_sessionmaker(bind=ENGINE)
