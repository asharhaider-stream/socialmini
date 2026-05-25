from fastapi import FastAPI
from app.cache import client
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/ping")
def ping():
    client.set("test", "redis is working!")
    return {"message": client.get("test")}

