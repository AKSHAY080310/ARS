from backend.db import get_connection
def log_interaction(user_id,movie_id,action):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO interactions(
        user_id,movie_id,action
    ) VALUES (?,?,?)""", (user_id,movie_id,action))
    conn.commit()
    conn.close()
    
def get_user_interactions(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT movie_id, action, timestamp
                   FROM interactions
                   WHERE user_id = ? ORDER BY timestamo DESC""",(user_id,))
    interactions = cursor.fetchall()
    conn.close()
    return interactions

def count_user_interactions(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*) FROM interactions
                   WHERE user_id = ?""",(user_id,))
    count=cursor.fetchone()[0]
    conn.close()
    return count

def get_interacted_movie_ids(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT DISTINCT movie_id FROM interactions
                   WHERE user_id = ?""",(user_id,))
    movies = cursor.fetchall()
    conn.close()
    return [movie[0] for movie in movies]
    
    
        
