import uvicorn
from fastapi import FastAPI

from database import engine
from models import Base
from user_router import users_router

app = FastAPI()
app.include_router(users_router)
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
