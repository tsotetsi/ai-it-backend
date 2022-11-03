from sqlalchemy.orm import Session

from api_sql.models import Tracker, User


class TrackerService:
    """TrackerService for tracker CRUD."""

    @staticmethod
    async def create(tracker, db: Session):
        new_tracker = Tracker(
            title=tracker.title,
            description=tracker.description,
            url=tracker.url,
            user_id=tracker.user_id
        )
        db.add(new_tracker)
        db.commit()
        return new_tracker

    """
    Get all user trackers.
    """
    @staticmethod
    def fetch_all_user_trackers(user_id: int, db: Session):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return db.query(Tracker).filter(Tracker.user_id == user.id).all()
        return []

    """
    Upload tracker attachment.
    """
    @staticmethod
    def upload_attachment(tracker_id, file, db: Session):
        return "Success"
