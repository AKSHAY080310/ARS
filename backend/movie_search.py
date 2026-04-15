from backend.db import get_connection


def search_movies(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT movie_id, title
        FROM movies
        WHERE title LIKE ?
        LIMIT 10
    """, ('%' + query + '%',))

    results = cursor.fetchall()
    conn.close()
    return results