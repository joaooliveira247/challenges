from typing import Annotated, TypeAlias

from fastapi import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from bank_api.core.database import get_session

DatabaseDependency: TypeAlias = Annotated[AsyncSession, Depends(get_session)]
