import logging
import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DB_URI = os.getenv("DB_URI")

if not DB_URI:
    logging.critical("Missing DB_URI environment variable.")
    raise SystemExit(1)

engine = create_async_engine(DB_URI)

AsyncSession = async_sessionmaker(engine)
