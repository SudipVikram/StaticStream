import bcrypt
from database.db import get_cursor

def verify_user(username, password):
    cursor, _ = get_cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",(username,)
    )
    result = cursor.fetchone()

    if not result:
        return False

    stored_hash = result[0]

    return bcrypt.checkpw(password.encode(),stored_hash)