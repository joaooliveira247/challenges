from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_NAME: str = Field(alias="APP_NAME", default="MyAPP")
    API_HOST: str = Field(alias="APP_HOST", default="localhost")
    API_PORT: int = Field(alias="APP_PORT", default=8000)
    API_PATH: str = Field(alias="APP_PATH", default="/api")
    API_MODE: str = Field(alias="APP_MODE", default="dev")

    DB_USER: str | None = None
    DB_PASSWD: str | None = None
    DB_CONTAINER_HOST: str | None = None
    DB_HOST: str | None = None
    DB_PORT: str | None = None
    DB_NAME: str | None = None

    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = "HS256"
    JWT_DEFAULT_LIFE_TIME: float = 360

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def postgres_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWD}@{self.DB_CONTAINER_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def postgres_local_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def fastapi_mode_config(self) -> dict:
        if self.API_MODE == "dev":
            return {
                "docs_url": "/docs",
                "redoc_url": "/redoc",
                "openapi_url": "/openapi.json",
            }
        return {
            "docs_url": None,
            "redoc_url": None,
            "openapi_url": None,
        }


@lru_cache
def get_settings() -> Settings:
    settings_instance = Settings()
    return settings_instance
