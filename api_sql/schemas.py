from datetime import datetime
from pydantic import BaseModel, EmailStr


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

