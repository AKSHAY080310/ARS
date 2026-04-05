from backend.db import get_connection
import pandas as pd
import os
def add_rating(user_id,movie_id,rating):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT  * FROM ratings
                   WHERE user_id=? AND movie_id=?""",
                   (user_id,movie_id))
    exist=cursor.fetchone()
    if exist:
        cursor.execute("""UPDATE ratings
                       SET rating=? WHERE
                       user_id=? AND movie_id=?""",
                       (rating,user_id,movie_id))
    else:
        cursor.execute("""INSERT INTO ratings (user_id,movie_id,rating)
                       VALUES (?,?,?)""",
                       (user_id,movie_id,rating))
    conn.commit()
    conn.close()
    
def load_ratings():
    df=pd.read_pickle(os.path.join("data","processed","movielens_for_collaborative.pkl"))
    
    ratings=df[["user_id","item_id","rating"]]
    conn=get_connection()
    cursor=conn.cursor()
    for _,row in ratings.iterrows():
        cursor.execute("""INSERT OR IGNORE INTO ratings (user_id,movie_id, rating)
                       VALUES(?,?,?)""",
                       (
                        int(row["user_id"]),
                        int(row["item_id"]),
                        float(row["rating"]))
        )
    conn.commit()
    conn.close()
    print("ratings loaded successfully")    
                