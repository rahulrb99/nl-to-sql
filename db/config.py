"""Database connection configuration from environment variables."""
import os

# Optional: load .env if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_connection_params():
    """Return PostgreSQL connection params from environment."""
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "database": os.getenv("DB_NAME", "nl2sql"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", ""),
    }
