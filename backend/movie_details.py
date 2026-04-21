from backend.db import get_connection
def get_movie_details(movie_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT movie_id, title, genres, overview, cast_names, director, language
                   FROM movies
                   WHERE movie_id=?""",(movie_id,)
                   )
    movie = cursor.fetchone()
    conn.close()
    if movie:
        return {
            "movie_id": movie[0],
            "title": movie[1],
            "genres": movie[2],
            "overview": movie[3],
            "cast_names": movie[4],
            "director": movie[5],
            "language": movie[6]
        }
    return movie    