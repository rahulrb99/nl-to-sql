import psycopg2
from psycopg2.extras import RealDictCursor

def execute_sql(sql: str):
    """
    Executes a validated SELECT SQL query and returns rows.
    """
    conn = psycopg2.connect(
        host="localhost",
        database="nl2sql",      # your DB name
        user="postgres",
        password="Edgeverve@1234"
    )

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            results = cur.fetchall()
            return results
    finally:
        conn.close()
