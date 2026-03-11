import sqlite3
import os

db_path = os.path.abspath("cms.db")
print("Creating database at:",db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    slug TEXT UNIQUE,
    meta TEXT,
    content TEXT,
    excerpt TEXT,
    created_at TEXT,
    published INGETER
)
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")
conn.commit()
conn.close()

print("Database successfully initialized")