from backend.db import get_connection
import sqlite3

def add_user(
    username,
    password,
    age,
    gender,
    occupation,
    preferred_language
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO users
            (
                username,
                password,
                age,
                gender,
                occupation,
                preferred_language
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            username,
            password,
            age,
            gender,
            occupation,
            preferred_language
        ))

        conn.commit()

        return "User created successfully"

    except sqlite3.IntegrityError:

        return "Username already exists"

    finally:

        conn.close()
        
def login_user(username,password):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        SELECT user_id, age, gender, occupation, preferred_language
        FROM users
        WHERE username = ? AND password = ?
    """, (username, password))
        
    user=cursor.fetchone()
    conn.close()
    if user:

        return {
            "user_id": user[0],
            "age": user[1],
            "gender": user[2],
            "occupation": user[3],
            "preferred_language": user[4]
        }

    return None  