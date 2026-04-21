from typing import Annotated

from fastapi import Depends

from bank_api.core.security import oauth2_schema

TokenDependency = Annotated[str, Depends(oauth2_schema)]
