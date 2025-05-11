from app.database import database
from app.models import users, posts
from app.schemas import UserCreate, PostCreate

async def create_user(user: UserCreate):
    query = users.insert().values(name=user.name)
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}

async def get_users():
    query = users.select()
    return await database.fetch_all(query)

async def create_post(post: PostCreate):
    query = posts.insert().values(title=post.title, user_id=post.user_id)
    post_id = await database.execute(query)
    return {**post.dict(), "id": post_id}

async def patch_post(post_id: int, title: str):
    query = posts.update().where(posts.c.id == post_id).values(title=title)
    await database.execute(query)
    return {"id": post_id, "title": title}

async def delete_post(post_id: int):
    query = posts.delete().where(posts.c.id == post_id)
    await database.execute(query)
    return {"deleted": post_id}

async def delete_post(post_id: int):
    query = posts.delete().where(posts.c.id == post_id)
    await database.execute(query)
    return {"deleted": post_id}
