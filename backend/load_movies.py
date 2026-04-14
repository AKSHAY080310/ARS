import pandas as pd
import os
from db import get_connection

df=pd.read_pickle(os.path.join("data","processed","tmdb_for_content.pkl"))
movies=df.drop_duplicates(subset=["tmdb_id"])

conn=get_connection()
cursor=conn.cursor()
for _,row in movies.iterrows():
    cursor.execute("""INSERT OR IGNORE INTO MOVIES (
        movie_id,title,language,genres,popularity,vote_average,vote_count,overview,cast_names,director,keywords,year,combined_features
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            row["tmdb_id"],
            row["title"],
            row["language"],
            row.get("genres",None),
            row.get("popularity",None),
            row.get("vote_average",None),
            row.get("vote_count",None),
            row.get("overview",None),
            row.get("cast",None),
            row.get("director",None),
            row.get("keywords",None),
            row.get("release_year",None),
            row.get("combined_features",None)
        )
    )
    
conn.commit()
conn.close()
print("Movies inserted successfully")