from fastapi import APIRouter
from app.cache import cache_user_profile, get_cached_user
from pydantic import BaseModel

router = APIRouter()

class UserProfile(BaseModel):
    user_id: str
    username: str
    email: str
    age: int
    bio: str

@router.get("/users/{user_id}")
def get_user(user_id):
    return get_cached_user(user_id)

@router.post("/users")
def store_user(user: UserProfile):
    return cache_user_profile(user.user_id, user.username, user.email, user.age, user.bio)
