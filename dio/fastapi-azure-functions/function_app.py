import logging
import azure.functions as func
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from azure.functions._http import HttpResponse
from starlette.types import ASGIApp, Receive, Scope, Send
import json

app = FastAPI()

# Create your FastAPI routes
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Azure Functions"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": f"Item {item_id}"}

# Convert Azure Function to ASGI handler for FastAPI
class AzureFunctionAsgiMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, req: func.HttpRequest) -> HttpResponse:
        scope = {
            "type": "http",
            "http_version": "1.1",
            "method": req.method,
            "headers": [(k.encode("utf-8"), v.encode("utf-8")) for k, v in req.headers.items()],
            "path": req.route_params.get("route", ""),
            "query_string": req.url.split('?')[-1].encode(),
            "server": ("localhost", 80),
            "client": (req.headers.get("X-Forwarded-For", req.remote_addr), req.headers.get("X-Forwarded-Port", req.port))
        }

        receive: Receive = lambda: req.get_json()
        send: Send = None

        # Run FastAPI app and capture the response
        response = await self.app(scope, receive, send)
        body = json.dumps(response.body).encode()

        return func.HttpResponse(body, status_code=response.status_code, mimetype="application/json")

# Use the AzureFunctionAsgiMiddleware to wrap FastAPI for Azure Functions
asgi_middleware = AzureFunctionAsgiMiddleware(app)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return asgi_middleware(req)
