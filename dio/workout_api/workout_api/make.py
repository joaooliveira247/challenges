import uvicorn
from alembic import command
from alembic.config import Config
from typer import Typer

from workout_api.core import BASE_DIR

cli = Typer(name="CLI for workout API")
alembic_cfg = Config(f"{BASE_DIR / 'alembic.ini'}")


@cli.command()
def run() -> None:
    uvicorn.run(
        "workout_api.api:app",
        log_level="info",
        reload=True,
    )


@cli.command()
def create_migrations(autogenerate: bool, msg: str) -> None:
    command.revision(alembic_cfg, autogenerate=autogenerate, message=msg)


@cli.command()
def run_migrations() -> None:
    command.upgrade(alembic_cfg, "head")
