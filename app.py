from typing import List

from fastapi import FastAPI, status, Depends, File, UploadFile
from sqlalchemy.orm import Session

from api_sql import models
from services.user_service import UserService
from services.tracker_service import TrackerService
from services.comment_service import CommentService
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


@app.get("/users/{_id}", tags=["Users"], response_model=List[schemas.User], status_code=status.HTTP_200_OK)
async def get_user(_id: int, db: Session = Depends(get_db)):
    """
    Get user details.
    :param _id: user db id.
    :param db: db connections instance.
    :return: str.
    """
    return UserService.fetch_by_id(db, _id)


@app.post("/trackers", tags=["Trackers"], response_model=schemas.Tracker, status_code=status.HTTP_201_CREATED)
async def create_tracker(tracker_request: schemas.TrackerCreate, db: Session = Depends(get_db)):
    """
    Create user tracker.
    :param tracker_request: request data.
    :param db: db connection instance.
    :return: str.
    """
    return await TrackerService.create(tracker_request, db)


@app.get("/trackers/fetch_all/{user_id}", tags=["Trackers"], response_model=List[schemas.Tracker], status_code=status.HTTP_200_OK)
async def fetch_all(user_id: int, db: Session = Depends(get_db)):
    """
    Fetch user trackers.
    :param user_id: logged-in user_id
    :param db: db connections instance.
    :return: str.
    """
    return TrackerService.fetch_all_user_trackers(user_id, db)


@app.post("/trackers/upload_file/{tracker_id}", tags=["Trackers"], status_code=status.HTTP_201_CREATED)
def upload_file(tracker_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    return TrackerService.upload_attachment(tracker_id, file, db)


@app.post("/trackers/comments", tags=["Trackers"], response_model=schemas.Comment, status_code=status.HTTP_201_CREATED)
async def comments(comment_request: schemas.CommentCreate, db: Session = Depends(get_db)):
    """
    Create tracker comment.
    :param comment_request: request data.
    :param db: db connection instance.
    :return: str.
    """
    return await CommentService.create(comment_request, db)


@app.post("/trackers/comments/fetch_tracker_comments",
          tags=["Trackers"],
          response_model=List[schemas.Comment],
          status_code=status.HTTP_200_OK)
async def fetch_all_tracker_comments(tracker_id: int, user_id: int, db: Session = Depends(get_db)):
    """
    Fetch tracker comments.
    :param tracker_id: trackeid
    :param user_id: user_id
    :param db: db connection instance.
    :return: str
    """
    return CommentService.fetch_all_tracker_comments(tracker_id, user_id, db)
