import os

from dotenv import load_dotenv

load_dotenv()

# Constants for creating access and refresh tokens.
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']   # should be kept secret

# Database Settings(POSTGRESQL).

DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_USERNAME = os.environ['DATABASE_USERNAME']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_PORT = os.environ['DATABASE_PORT']

SQLALCHEMY_DATABASE_URL = "postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}".format(
    db_username=DATABASE_USERNAME,
    db_password=DATABASE_PASSWORD,
    db_host=DATABASE_HOST,
    db_port=DATABASE_PORT,
    db_name=DATABASE_NAME
)
