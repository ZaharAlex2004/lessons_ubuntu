from fastapi import FastAPI, BackgroundTasks, WebSocket
from db import database, engine, metadata
from schemas import UserCreate, PostCreate
import crud
import asyncio

app = FastAPI()

metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

def fake_background_task(message: str):
    import time
    time.sleep(5)
    print(f"Background: {message}")

@app.post("/users/")
async def create_user(user: UserCreate):
    return await crud.create_user(user)

@app.get("/users/")
async def list_users():
    return await crud.get_users()

@app.post("/posts/")
async def create_post(post: PostCreate, background_tasks: BackgroundTasks):
    background_tasks.add_task(fake_background_task, f"New post: {post.title}")
    return await crud.create_post(post)

@app.patch("/posts/{post_id}")
async def update_post(post_id: int, title: str):
    return await crud.patch_post(post_id, title)

@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    return await crud.delete_post(post_id)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")


