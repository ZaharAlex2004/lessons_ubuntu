from fastapi import FastAPI, BackgroundTasks, WebSocket, Depends, APIRouter
from sqlalchemy.orm import Session
from app.schemas import UserCreate, PostCreate
from app import crud

router = APIRouter()

def fake_background_task(message: str):
    import time
    time.sleep(5)
    print(f"Background: {message}")

@router.post("/users/")
async def create_user(user: UserCreate):
    return await crud.create_user(user)

@router.get("/users/")
async def list_users():
    return await crud.get_users()

@router.post("/posts/")
async def create_post(post: PostCreate, background_tasks: BackgroundTasks):
    background_tasks.add_task(fake_background_task, f"New post: {post.title}")
    return await crud.create_post(post)

@router.patch("/posts/{post_id}")
async def update_post(post_id: int, title: str):
    return await crud.patch_post(post_id, title)

@router.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    return await crud.delete_post(post_id)

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
