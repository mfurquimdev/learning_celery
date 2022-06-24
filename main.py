import uvicorn
from fastapi import FastAPI

from app.messaging.view import router as messaging_router

app = FastAPI()

app.include_router(messaging_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)
