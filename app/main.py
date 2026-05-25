from fastapi import FastAPI
from app.cache.user_cache import client
from app.routes.user_routes import router
from app.routes.post_routes import router as post_router

app = FastAPI()

app.include_router(router)
app.include_router(post_router)

@app.get("/ping")
def ping():
    client.set("test", "redis is working!")
    return {"message": client.get("test")}

