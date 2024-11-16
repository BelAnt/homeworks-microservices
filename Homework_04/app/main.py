from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.endpoints import users
from app.db import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    print("DB connected!")
    yield
    await database.disconnect()
    print("DB disconnected!")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"This is CRUD API"}


app.include_router(users.router, prefix="/api/user", tags=["user"])
