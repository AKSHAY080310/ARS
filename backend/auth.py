from backend.db import get_connection
import sqlite3

def add_user(username, password):
    conn=get_connection()
    cursor=conn.cursor()
    
    try:
        cursor.execute("""INSERT INTO users (username,password)
                       VALUES (?,?)""",(username,password))
        
        conn.commit()
        return "User created successfully"
    
    except sqlite3.IntegrityError:
        return "Username already exists"
    
    finally:
        conn.close()
        
def login_user(username,password):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT user_id FROM users WHERE username=? AND password=?
                    """,(username,password))
        
    user=cursor.fetchone()
    conn.close()
    if user:
        return user[0]
    else:
        return None    