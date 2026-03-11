import os
import bcrypt
import sqlite3

# connecting to the database
db_path = os.path.abspath("cms.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# superuser credentials
username = "admin"
password = "admin123"
role = "superuser"

# editor credentials
editorusername = "editor"
editorpassword = "editor123"
editorrole = "editor"

# writer credentials
writerusername = "writer"
writerpassword = "writer123"
writerrole = "writer"

# hash password
hashed_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
editor_password = bcrypt.hashpw(editorpassword.encode(),bcrypt.gensalt())
writer_password = bcrypt.hashpw(writerpassword.encode(),bcrypt.gensalt())


# insert superuser
'''cursor.execute(
    "INSERT INTO users(username, password, role) VALUES(?,?,?)",
    (username, hashed_password, role)
)'''

# insert editor
cursor.execute(
    "INSERT INTO users(username, password, role) VALUES(?,?,?)",
    (editorusername, editor_password, editorrole)
)

# insert writer
cursor.execute(
    "INSERT INTO users(username, password, role) VALUES(?,?,?)",
    (writerusername, writer_password, writerrole)
)

conn.commit()

print("User created successfully")
