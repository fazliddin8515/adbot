from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.db import create_db_url
from utils.env import get_env

DB_USER = get_env("DB_USER")
DB_PASS = get_env("DB_PASS")
DB_HOST = get_env("DB_HOST")
DB_PORT = get_env("DB_PORT")
DB_NAME = get_env("DB_NAME")

DB_URL = create_db_url("mysql+pymysql", DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

engine = create_engine(DB_URL)

Session = sessionmaker(engine)
