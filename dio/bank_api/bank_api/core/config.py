from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = Field(alias="APP_NAME", default="MyAPP")
    API_HOST: str = Field(alias="APP_HOST", default="localhost")
    API_PORT: int = Field(alias="APP_PORT", default=8000)
    API_PATH: str = Field(alias="APP_PATH", default="/api/")

    DB_USER: str | None = None
    DB_PASSWD: str | None = None
    DB_HOST: str | None = None
    DB_PORT: str | None = None
    DB_NAME: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def postgres_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


@lru_cache
def get_settings() -> Settings:
    a = Settings()
    print(a.postgres_dsn)
    return a
