import sqlite3
import os
db_path=os.path.join("data","database","movie.db")

def get_connection():
    conn=sqlite3.connect(db_path)
    return conn

def get_path():
    return db_path