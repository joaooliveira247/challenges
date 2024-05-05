from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv
from pathlib import Path

BASE_DIR: Path = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    DB_URL: str


settings = Settings()
