from typing import Union, Any

from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .utils import (
    ALGORITHM,
    JWT_SECRET_KEY
)

from jose import jwt
from pydantic import ValidationError
from api_sql.schemas import TokenPayLoad, User

from sqlalchemy.orm import Session
from services.user_service import UserService
from db import get_db


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/users/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(
            token=token, key=JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayLoad(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    user: Union[dict[str, Any], None] = UserService.fetch_by_email(db, token_data.sub) or None

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user."
        )

    return user
