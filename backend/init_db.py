import sqlite3
from backend.db import get_connection,get_path

conn=get_connection()
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT,
    age INTEGER,
    gender TEXT,
    occupation TEXT,
    preferred_language TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    language TEXT,
    genres TEXT,
    popularity REAL,
    vote_average REAL,
    vote_count INTEGER,
    overview TEXT,
    cast_names TEXT,
    director TEXT,
    keywords TEXT,
    year INTEGER,
    combined_features TEXT
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