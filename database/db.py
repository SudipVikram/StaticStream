import sqlite3
import os

# database file called throughout the cms for connection requests

def get_connection():
    db_path = os.path.abspath("cms.db")
    return sqlite3.connect(db_path,check_same_thread=False)

def get_cursor():
    conn = get_connection()
    return conn.cursor(),conn