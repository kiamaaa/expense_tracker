import sqlite3

import config


def get_connection(db_path=None):
    
    conn = sqlite3.connect(db_path or config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row            # rows behave like dicts: row["amount_cents"]
    conn.execute("PRAGMA foreign_keys = ON")  # SQLite ignores foreign keys unless enabled per connection
    return conn


def init_db(db_path=None):
   
    schema = config.SCHEMA_PATH.read_text()
    conn = get_connection(db_path)
    try:
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()