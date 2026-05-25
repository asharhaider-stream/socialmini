from fastapi import FastAPI
from app.cache import client

app = FastAPI()

@app.get("/ping")
def ping():
    client.set("test", "redis is working!")
    return {"message": client.get("test")}