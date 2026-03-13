from database import get_connection

def register_user(username,email,password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
    "INSERT INTO users(username,email,password) VALUES(?,?,?)",
    (username,email,password)
    )

    conn.commit()
    conn.close()


def login_user(email,password):

    conn = get_connection()
    cur = conn.cursor()

    user = cur.execute(
    "SELECT * FROM users WHERE email=? AND password=?",
    (email,password)
    ).fetchone()

    conn.close()

    return user