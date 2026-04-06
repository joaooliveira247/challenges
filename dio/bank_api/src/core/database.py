from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core.config import get_settings

settings = get_settings()

engine: AsyncEngine = create_async_engine(settings.postgres_dsn)

async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
