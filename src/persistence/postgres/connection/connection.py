from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.config import ENV_CONFIG

USERNAME = ENV_CONFIG.POSTGRES_USER
PASSWORD = ENV_CONFIG.POSTGRES_PASSWORD
DB_ADDRESS = ENV_CONFIG.POSTGRES_DB_ADDRESS
DB_PORT = ENV_CONFIG.POSTGRES_DB_PORT
DB_NAME = ENV_CONFIG.POSTGRES_DB

ENGINE = create_async_engine(f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{DB_ADDRESS}:{DB_PORT}/{DB_NAME}")

AsyncSession = async_sessionmaker(bind=ENGINE)
