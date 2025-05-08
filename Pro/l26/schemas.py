from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str

class User(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class PostCreate(BaseModel):
    title: str
    user_id: int

class Post(BaseModel):
    id: int
    title: str
    user_id: int

    class Config:
        orm_mode = True
