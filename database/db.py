import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.db import create_db_url

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

assert DB_USER is not None, "DB_USER environment variable is required"
assert DB_PASS is not None, "DB_PASS environment variable is required"
assert DB_HOST is not None, "DB_HOST environment variable is required"
assert DB_PORT is not None, "DB_PORT environment variable is required"
assert DB_NAME is not None, "DB_NAME environment variable is required"

DB_URL = create_db_url(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME,
)

engine = create_engine(DB_URL)

Session = sessionmaker(engine)
