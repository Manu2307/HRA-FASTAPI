from fastapi import FastAPI
import uvicorn
from app.api import API_ROUTERS


app = FastAPI()

@app.get('/ping')
def ping():
    return {"message": "pong"}


for router, kwargs in API_ROUTERS:
    app.include_router(router, **kwargs)

if __name__ == "__main__":
    uvicorn.run(app, port=5000, reload=True)
