import bcrypt
from database.db import get_cursor

# function to verify the username and password
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

# function to get the role of the user
def get_role(username):
    cursor, _ = get_cursor()

    cursor.execute(
        "SELECT role from users WHERE username = ?",(username,)
    )
    result = cursor.fetchone()
    if not result:
        return False

    return result