import sqlite3

DB_NAME = "app.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS businesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_business(description: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO businesses (description) VALUES (?)",
        (description,)
    )

    conn.commit()
    conn.close()

def get_all_businesses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, description FROM businesses")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"id": row[0], "description": row[1]}
        for row in rows
    ]