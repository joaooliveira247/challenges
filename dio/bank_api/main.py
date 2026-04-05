from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_fast_api():
    return {"message": "Hello World!"}
