from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from utils.env import get_env

DB_USER = get_env("DB_USER")
DB_PASS = get_env("DB_PASS")
DB_HOST = get_env("DB_HOST")
DB_PORT = get_env("DB_PORT")
DB_NAME = get_env("DB_NAME")

DB_URL = URL.create("mysql+pymysql", DB_USER, DB_PASS, DB_HOST, int(DB_PORT), DB_NAME)

engine = create_engine(DB_URL)
