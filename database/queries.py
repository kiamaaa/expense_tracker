import sqlite3
import config



def add_category(conn,name):
    cur = conn.execute("INSERT INTO categories (name) VALUES(?)",(name,))
    conn.commit() 
    return cur.lastrowid

def get_category_by_name(conn,name):
    result = conn.execute("SELECT id,name FROM categories WHERE name = ?", (name,)).fetchone()
    return result


def get_or_create_category(conn,name):
    row = get_category_by_name(conn,name)
    if row is not None:
        return row["id"]
    return add_category(conn,name)


def list_categories(conn):
    result = conn.execute("SELECT id,name FROM categories ORDER BY name").fetchall()
    return result



