import psycopg2
from psycopg2.extras import RealDictCursor

from db.config import get_connection_params


def execute_sql(sql: str):
    """
    Executes a validated SELECT SQL query and returns rows.
    """
    conn = psycopg2.connect(**get_connection_params())

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            results = cur.fetchall()
            return results
    finally:
        conn.close()
