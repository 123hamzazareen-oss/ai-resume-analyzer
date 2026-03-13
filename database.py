import sqlite3

def get_connection():

    conn = sqlite3.connect("database.db")
    return conn


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skills TEXT,
        score TEXT,
        missing_skills TEXT,
        suggestions TEXT,
        jobs TEXT
    )
    """)

    conn.commit()
    conn.close()