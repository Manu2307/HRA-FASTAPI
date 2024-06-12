import logging.config
from fastapi import FastAPI
import uvicorn
from app.api import API_ROUTERS
from logging_config.config import LOGGING_CONF
from starlette.middleware.base import BaseHTTPMiddleware
from middlewares.logging_middleware import logging_middleware

logging.config.dictConfig(LOGGING_CONF)

app = FastAPI()

for router, kwargs in API_ROUTERS:
    app.include_router(router, **kwargs)

app.add_middleware(BaseHTTPMiddleware, dispatch=logging_middleware)


@app.get('/ping', tags=['Server Check'])
def ping():
    return {"message": "Hey People! The server is Ready"}


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
