import redis

client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def cache_user_profile(user_id, username,email,age,bio):
    client.hset(f"user:{user_id}", mapping={"username": username, "email": email, "age": age, "bio": bio})
    client.expire(f"user:{user_id}", 3600)
    return {"message": "user cached successfully"}
    

def get_cached_user(user_id):
    return client.hgetall(f"user:{user_id}")

def delete_cached_user(user_id):
    client.delete(f"user:{user_id}")