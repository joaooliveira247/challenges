from fastapi import FastAPI

from bank_api.core.config import get_settings
from bank_api.urls import api_router

settings = get_settings()

app = FastAPI(
    title=settings.API_NAME,
    **settings.fastapi_mode_config
)
app.include_router(api_router)


@app.get("/")
async def hello_fast_api():
    return {"message": "Hello World!"}
