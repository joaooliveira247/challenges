from typer import Typer
import uvicorn

cli = Typer(name="CLI for workout API")


@cli.command()
def run() -> None:
    uvicorn.run(
        "workout_api.api:app",
        log_level="info",
        reload=True,
    )
