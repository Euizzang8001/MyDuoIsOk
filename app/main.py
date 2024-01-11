from fastapi import FastAPI
from app.routers.search import router

app = FastAPI()

app.include_router(router)