from sqlalchemy.engine import URL


def create_db_url(
    drivername: str, username: str, password: str, host: str, port: str, database: str
) -> URL:
    return URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=host,
        port=int(port),
        database=database,
    )
