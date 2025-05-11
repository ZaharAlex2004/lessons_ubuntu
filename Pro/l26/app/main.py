from fastapi import FastAPI, BackgroundTasks, WebSocket
from sqlalchemy import Table, Column, Integer, String
from app.database import database, engine, metadata
from app.schemas import UserCreate, PostCreate
from app.routers import accounts
import app.crud

app = FastAPI()

app.include_router(accounts.router)

metadata.create_all(engine)