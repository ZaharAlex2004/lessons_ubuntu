from sqlalchemy import Table, Column, Integer, String, ForeignKey
from app.database import metadata
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("user_id", Integer, ForeignKey("users.id")),
)

tags = Table(
    "tags",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True, nullable=False),
)

post_tags = Table(
    "post_tags",
    metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)