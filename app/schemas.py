from pydantic import BaseModel
from datetime import datetime

class UserProfile(BaseModel):
    user_id: str
    username: str
    email: str
    age: int
    bio: str
    
class UserPost(BaseModel):
    post_id: str
    user_id: str
    title: str
    content: str 
    description: str
    timestamp: datetime   