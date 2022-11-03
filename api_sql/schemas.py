from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, AnyUrl


class UserBase(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    created: datetime
    modified: datetime

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    """
    Schema for creating a new user.
    """
    pass


class CommentBase(BaseModel):
    """
    Schema for adding a new comment.
    """
    text: str
    tracker_id: int


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    created: datetime

    class Config:
        orm_mode = True


class TrackerBase(BaseModel):
    """
    Schema for creating a new tracker.
    """
    title: str
    description: str | None = None
    url: AnyUrl | None = None


class Tracker(TrackerBase):
    id: int
    attachment: AnyUrl | None = None
    user_id: int
    created: datetime
    modified: datetime

    class Config:
        orm_mode = True


class TrackerCreate(TrackerBase):
    user_id: int

