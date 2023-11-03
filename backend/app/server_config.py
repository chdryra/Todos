import os
from dataclasses import dataclass

from sql.sqlutils import PostgresDb


@dataclass
class ServerConfig:
    ip: str
    port: int


def get_db() -> PostgresDb:
    return PostgresDb(get_db_uri())


def get_db_uri() -> str:
    env = os.environ.get("SERVER_ENV")
    user = os.environ["DB_USER"]
    pw = os.environ["DB_PASSWORD"]

    db = "postgresql://" + user + ":" + pw + "@"
    port = 5432
    match env:
        case "LOCAL":
            server = f"127.0.0.1:{port}"
        case "LOCAL_DOCKER":
            server = f"host.docker.internal:{port}"
        case "CLOUD":
            server = f"127.0.0.1:{port}"
        case _:
            server = f"127.0.0.1:{port}"

    return db + server + "/notes"
