from backend.db import get_connection


def add_rating(user_id, movie_id, rating):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT rating FROM ratings
        WHERE user_id = ? AND movie_id = ?
    """, (user_id, movie_id))

    existing = cursor.fetchone()

    if existing:

        cursor.execute("""
            UPDATE ratings
            SET rating = ?
            WHERE user_id = ? AND movie_id = ?
        """, (rating, user_id, movie_id))

    else:

        cursor.execute("""
            INSERT INTO ratings (user_id, movie_id, rating)
            VALUES (?, ?, ?)
        """, (user_id, movie_id, rating))

    conn.commit()
    conn.close()