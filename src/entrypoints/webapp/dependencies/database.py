from src.persistence.postgres.connection.connection import AsyncSession

async def get_db_session():
    session = AsyncSession()
    try:
        yield session
    except Exception as exc:
        await session.rollback()
        raise exc
    else:
        await session.commit()
    finally:
        await session.close()
