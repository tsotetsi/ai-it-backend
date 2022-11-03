from sqlalchemy.orm import Session
from sqlalchemy import select

from api_sql.models import User


class UserService:
    """UserService for user CRUD."""

    """
    Create a new user.
    """
    @staticmethod
    async def create(user, db: Session):
        new_user = User(
            name=user.name,
            surname=user.surname,
            email=user.email,
            password=user.password
        )
        db.add(new_user)
        db.commit()
        return new_user

    """
    Get specific user.
    """
    @staticmethod
    def fetch_by_id(db: Session, _id):
        user = db.query(User).filter(User.id == _id).all()
        if user:
            return user
        return []

    """
    Get all users.
    """
    @staticmethod
    def fetch_all(db: Session):
        return db.query(User).all()
