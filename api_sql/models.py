from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP


from db import Base


class User(Base):
    """
    User database model.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    created = Column(TIMESTAMP, nullable=False, default=datetime.now())
    modified = Column(TIMESTAMP, nullable=False, default=datetime.now())

    def __repr__(self):
        return 'UserModel(id=%s, name=%s, surname=%s, created=%s, modified=%s)' % (self.id, self.name, self.surname, self.created, self.modified)


class Comment(Base):
    """
    A comment database model.
    """
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    tracker_id = Column(Integer, ForeignKey("trackers.id"))
    created = Column(TIMESTAMP, nullable=False, default=datetime.now())

    def __repr__(self):
        return 'CommentModel(text=%s, tracker_id=%s)' % (self.text, self.tracker_id)


class Tracker(Base):
    """
    A tracking database model.
    """
    __tablename__ = "trackers"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True, default=None)
    url = Column(String, nullable=True, default=None)
    attachment = Column(String, nullable=True)
    created = Column(TIMESTAMP, nullable=False, default=datetime.now())
    modified = Column(TIMESTAMP, nullable=False, default=datetime.now())

    def __repr__(self):
        return 'TrackerModel(title=%s, description=%s)' % (self.title, self.description)
