from sqlalchemy.orm import Session


from api_sql.models import Comment


class CommentService:
    """CommentService for comment CRUD."""

    @staticmethod
    async def create(comment, db: Session):
        new_comment = Comment(
            text=comment.text,
            tracker_id=comment.tracker_id
        )
        db.add(new_comment)
        db.commit()
        return new_comment

    """
    Get all tracker comments.
    """

    @staticmethod
    def fetch_all_tracker_comments(tracker_id: int, db: Session):
        comments = db.query(Comment).filter(Comment.tracker_id == tracker_id).all()
        if comments:
            return comments
        return []
