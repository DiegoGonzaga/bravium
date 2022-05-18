from fastapi import FastAPI
from random import randint
from .routes import media

app = FastAPI()

app.include_router(media.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def root():
    return {"message": randint(0, 1000)}
