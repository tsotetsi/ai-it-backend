from datetime import datetime
from sqlalchemy import Column, Integer, String, DATETIME, CheckConstraint

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
    created = Column(DATETIME, nullable=False, default=datetime.now())
    modified = Column(DATETIME, nullable=False, default=datetime.now())

    def __repr__(self):
        return 'UserModel(name=%s, surname=%s, created=%s, modified=%s)' % (self.name, self.surname, self.created, self.modified)

