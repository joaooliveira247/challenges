from fastapi import FastAPI

from bank_api.core.config import get_settings

settings = get_settings()

app = FastAPI()


@app.get("/")
async def hello_fast_api():
    return {"message": "Hello World!"}
