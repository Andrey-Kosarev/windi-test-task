from src.persistence.postgres.connection.connection import AsyncSession

async def get_db_session():
    session = AsyncSession()
    try:
        yield session
    finally:
        await session.close()