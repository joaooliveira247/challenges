from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from src.core.config import get_settings

settings = get_settings()

engine: AsyncEngine = create_async_engine(settings.postgres_dsn)
