import psycopg2

def get_schema():
    conn = psycopg2.connect(
        host="localhost",
        database="nl2sql",      # your DB name
        user="postgres",
        password="Edgeverve@1234"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT
            table_name,
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'orders'
        ORDER BY ordinal_position;
    """)

    rows = cur.fetchall()

    schema_text = "Table: orders\nColumns:\n"
    for table, column, dtype in rows:
        schema_text += f"- {column} ({dtype})\n"

    cur.close()
    conn.close()

    return schema_text


if __name__ == "__main__":
    print(get_schema())
