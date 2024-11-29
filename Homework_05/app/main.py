from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.endpoints import users
from app.db import database
from prometheus_fastapi_instrumentator import Instrumentator, metrics


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    print("DB connected!")
    yield
    await database.disconnect()
    print("DB disconnected!")


app = FastAPI(lifespan=lifespan)
instrumentator = Instrumentator(excluded_handlers=["/metrics"]).instrument(app)
instrumentator.add(metrics.latency(buckets=(.005, .01, .025, .05, .075, .1, .25, .5, .75, 1.0, 2.5, 5.0, 7.5, 10.0)))
instrumentator.add(metrics.requests())
instrumentator.expose(app)

@app.get("/")
def read_root():
    return {"This is CRUD API"}


app.include_router(users.router, prefix="/api/user", tags=["user"])
