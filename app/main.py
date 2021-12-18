import uvicorn

from api.endpoints.user import users_router
from fastapi import FastAPI

app = FastAPI(prefix="api")
app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
