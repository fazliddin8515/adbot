from sqlalchemy.engine import URL


def create_db_url(
    drivername: str, username: str, password: str, host: str, port: int, database: str
) -> URL:
    return URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )
