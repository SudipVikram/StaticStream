import os
import bcrypt
import sqlite3

# connecting to the database
db_path = os.path.abspath("cms.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

username = "admin"
password = "admin123"
role = "superuser"

# hash password
hashed_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt())

# insert user
cursor.execute(
    "INSERT INTO users(username, password, role) VALUES(?,?,?)",
    (username, hashed_password, role)
)

conn.commit()

print("User created successfully")
