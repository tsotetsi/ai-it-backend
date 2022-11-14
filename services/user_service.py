from sqlalchemy.orm import Session

from api_sql.models import User
from auth.utils import get_hashed_password


class UserService:
    """UserService for user CRUD."""

    """
    Signup a new user.
    """
    @staticmethod
    async def signup(user, db: Session):
        new_user = User(
            name=user.name,
            surname=user.surname,
            email=user.email,
            password=get_hashed_password(user.password)
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

    """
    Get user by email.
    """
    @staticmethod
    def fetch_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
