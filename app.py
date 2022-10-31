from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session

from api_sql import models
from services.user_service import UserService
from db import get_db, engine
from api_sql import schemas


API_VERSION, API_ENV = "0.0.1", "development"


app = FastAPI(
    debug=True,
    title="Job Applications Management System.",
    description="Job Applications Management System.",
    version=API_VERSION
)

models.Base.metadata.create_all(bind=engine)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {
        "api_version": API_VERSION,
        "environment": API_ENV
    }


@app.post("/users", tags=["Users"], response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def create_user(user_request: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user
    :param user_request: user request data
    :param db: db connection instance
    :return: str
    """
    return await UserService.create(user_request, db)


@app.get("/users/{_id}", tags=["Users"], response_model=schemas.User)
async def get_user(_id: int, db: Session = Depends(get_db)):
    """
    Get user details.
    :param _id: user db id.
    :param db: db connections instance.
    :return: str
    """
    return UserService.fetch_by_id(db, id)
