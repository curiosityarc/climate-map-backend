from fastapi import FastAPI
from app.routes import map
from app.gee_client import init_gee

app = FastAPI()
init_gee()

app.include_router(map.router, prefix="/api")
