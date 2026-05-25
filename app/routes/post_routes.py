from fastapi import APIRouter
from app.schemas import UserPost
from app.cache.post_cache import cache_post, delete_cached_post, get_user_feed

router = APIRouter()

@router.post("/posts")
def create_post(post: UserPost):
    return cache_post(post.model_dump())

@router.get("/feed/{user_id}")
def get_feed(user_id: str):
    feed = get_user_feed(user_id)
    if feed:
        return {"source": "cache", "data": feed}
    return {"source": "db", "data": "would hit postgres here"}

@router.delete("/posts/{post_id}")
def delete_post(post_id: str, user_id: str):
    return delete_cached_post(user_id, post_id)


