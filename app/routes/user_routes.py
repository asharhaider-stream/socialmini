from fastapi import APIRouter
from app.cache.user_cache import cache_user_profile, delete_cached_user, get_cached_user
from app.schemas import UserProfile

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id):
    cached = get_cached_user(user_id)
    if cached:
        return {"source": "cache", "data": cached}
    return {"source": "db", "data": "would hit postgres here"}

@router.post("/users")
def store_user(user: UserProfile):
    return cache_user_profile(user.user_id, user.username, user.email, user.age, user.bio)

@router.put("/users/{user_id}")
def update_user(user: UserProfile):
    delete_cached_user(user.user_id)
    cache_user_profile(user.user_id, user.username, user.email, user.age, user.bio)
    
    return {"message": "User updated successfully"}
    
