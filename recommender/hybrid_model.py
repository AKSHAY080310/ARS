import pandas as pd
import os
from recommender.content_model import recommend_by_user_history
tmdb_df=pd.read_pickle(os.path.join("data","processed","tmdb_for_content.pkl"))
tmdb_df=tmdb_df.rename(columns={"tmdb_id":"movie_id"})
def hybrid_recommend(user_id,n=10):
    content_recs = recommend_by_user_history(user_id,n=30)
    if isinstance(content_recs, str):
        return content_recs
    content_recs = content_recs.copy()
    max_popularity = tmdb_df["popularity"].max()
    content_recs["popularity_score"]=(content_recs["movie_id"].map(
        tmdb_df.set_index("movie_id")["popularity"])/max_popularity)
    content_recs["vote_score"]=(content_recs["movie_id"].map(
        tmdb_df.set_index("movie_id")["vote_average"])/10)
    content_recs["hybrid_score"]=(0.6+0.2 * content_recs["popularity_score"] + 
                                  0.2* content_recs["vote_score"])
    content_recs=content_recs.sort_values(by="hybrid_score",ascending=False)
    return content_recs.head(n)[
        ["movie_id","title","genres","hybrid_score"]
    ]
    