import pandas as pd
from backend.db import get_connection
from sklearn.metrics.pairwise import cosine_similarity

def get_data():
    conn=get_connection()
    df=pd.read_sql_query("""
                        SELECT r.user_id,r.movie_id,r.rating
                        FROM ratings r
                        JOIN movies m ON r.movie_id=m.movie_id
                        """, conn)
    conn.close()
    return df

def create_pivot(df):
    pivot=df.pivot_table(index="user_id",columns="movie_id",values="rating").fillna(0)
    return pivot

def compute_similarity(pivot):
    similarity=cosine_similarity(pivot)
    similarity_df=pd.DataFrame(
        similarity,
        index=pivot.index,
        columns=pivot.index)
    return similarity_df
    
def recommend_movies(user_id,top_n=5):
    df=get_data()
    if user_id not in df["user_id"].values:
        return get_popular_movies()
    pivot=create_pivot(df)
    similarity_df=compute_similarity(pivot)
    similar_users=similarity_df[user_id].sort_values(ascending=False)[1:top_n+1]
    similar_users_ratings=pivot.loc[similar_users.index]
    scores=similar_users_ratings.T.dot(similar_users) / similar_users.sum()
    watched=pivot.loc[user_id]
    scores= scores[watched==0]
    scores=scores[scores>0]
    return scores.sort_values(ascending=False).head(top_n)

def get_popular_movies():
    df=get_data()
    popular=df.groupby("title")["rating"].mean().sort_values(ascending=False).head(10)
    return popular
        