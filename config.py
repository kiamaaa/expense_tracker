import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


DATABASE_PATH = Path(os.environ.get("EXPENSE_DB_PATH", BASE_DIR / "expenses.db"))
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100