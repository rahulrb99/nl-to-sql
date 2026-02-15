import re

# SQL keywords that must NEVER be allowed
FORBIDDEN_KEYWORDS = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE",
    "EXECUTE",
    "EXEC",
    "MERGE",
    "REPLACE",
]

# Match first SELECT statement: either "SELECT ... ;" or "SELECT ..." to end
_SELECT_PATTERN = re.compile(
    r"\bSELECT\b.*?;|\bSELECT\b.*",
    re.IGNORECASE | re.DOTALL,
)


def extract_sql(text: str) -> str:
    """
    Cleans LLM output and extracts raw SQL.
    Removes markdown fences, then finds the first SELECT statement.
    """
    # Remove markdown code fences
    text = re.sub(r"```\s*sql\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```\s*", "", text)
    text = text.strip()

    # If it already starts with SELECT, use it (after stripping trailing ```)
    if text.upper().startswith("SELECT"):
        return text.strip()

    # Otherwise find first SELECT statement
    match = _SELECT_PATTERN.search(text)
    if match:
        return match.group(0).strip().rstrip(";").strip()

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
