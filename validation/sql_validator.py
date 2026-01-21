import re

# SQL keywords that must NEVER be allowed
FORBIDDEN_KEYWORDS = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE"
]


def extract_sql(text: str) -> str:
    """
    Cleans LLM output and extracts raw SQL.
    Removes markdown fences and extra text.
    """

    # Remove ```sql and ``` if present
    text = re.sub(r"```sql", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    return text.strip()


def validate_sql(sql: str) -> None:
    """
    Validates SQL for safety.
    Raises ValueError if SQL is unsafe.
    """

    sql_upper = sql.upper()

    # Only SELECT queries allowed
    if not sql_upper.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed")

    # Block dangerous SQL keywords
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_upper:
            raise ValueError(f"Forbidden SQL keyword detected: {keyword}")
