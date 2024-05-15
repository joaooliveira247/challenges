from fastapi import FastAPI
from store_api.core import settings
from store_api.urls import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
        )


app = App()
app.include_router(api_router)
