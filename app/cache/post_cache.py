from app.cache.user_cache import client

def cache_post(post: dict):
    
    timestamp = post["timestamp"]
    if hasattr(timestamp, 'timestamp'):
        score = timestamp.timestamp()
    else:
        score = float(timestamp)

    client.hset(f"post:{post['post_id']}", mapping={
        "user_id": post["user_id"],
        "title": post["title"],
        "content": post["content"],
        "description": post["description"],
        "timestamp": str(timestamp)
    })

    client.zadd(f"feed:{post['user_id']}", {post["post_id"]: score})
    client.expire(f"post:{post['post_id']}", 3600)
    return {"message": "post cached successfully"}
    
def get_user_feed(user_id):
    post_ids = client.zrevrange(f"feed:{user_id}", 0, -1)
    posts = []
    for post_id in post_ids:
        post = client.hgetall(f"post:{post_id}")
        posts.append(post)
    return posts    