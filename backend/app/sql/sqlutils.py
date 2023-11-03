# Note: the module name is psycopg, not psycopg3
import psycopg


class PostgresDb:
    def __init__(self, postgres_url: str) -> None:
        self.postgres_url = postgres_url

    def insert(self, sql: str):
        with psycopg.connect(f"{self.postgres_url}") as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit()
