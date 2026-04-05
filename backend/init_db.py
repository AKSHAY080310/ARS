import sqlite3
from backend.db import get_connection,get_path

conn=get_connection()
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT 
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
    movie_id INTEGER,
    title TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    overview TEXT,
    keywords TEXT,
    cast_names TEXT,
    director TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ratings(
    user_id INTEGER,
    movie_id INTEGER,
    rating REAL
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS interactions(
    interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    action TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
print("tables created successfully")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
print(get_path())
conn.close()