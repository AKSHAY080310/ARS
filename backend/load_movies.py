import pandas as pd
import os
from backend.db import get_connection

df=pd.read_pickle(os.path.join("data","processed","movielens_for_collaborative.pkl"))
movies=df[["item_id","clean_title","year","genre_label"]].drop_duplicates(subset=["item_id"])

conn=get_connection()
cursor=conn.cursor()
for _,row in movies.iterrows():
    cursor.execute("""INSERT OR IGNORE INTO MOVIES (
        movie_id,title,year,genre,overview,keywords,cast_names,director
        )
        VALUES(?,?,?,?,?,?,?,?)
        """, (
            row["item_id"],
            row["clean_title"],
            row["year"],
            row.get("genre_label",None),
            None,
            None,
            None,
            None
        )
    )
    
conn.commit()
conn.close()
print("Movies inserted successfully")