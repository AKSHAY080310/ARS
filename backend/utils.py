from backend.db import get_connection
def get_movie_id(title):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
                   SELECT movie_id FROM movies
                   WHERE title=?""",
                   (title))
    result=cursor.fetchone()
    conn.close()
    
    if result:
        return result[0]
    else:
        return None
    
def search_movies(query):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
                   SELECT movie_id,title,year
                   FROM movies
                   WHERE LOWER(title) LIKE LOWER(?)""",
                   (f"%{query}%",))
    results=cursor.fetchall()
    conn.close()
    return results    