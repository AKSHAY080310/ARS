import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity
movielens_df=pd.read_pickle(os.path.join("data","processed","movielens_for_collaborative.pkl"))
user_movie_matrix=movielens_df.pivot_table(
    index="user_id",
    columns="item_id",
    values="rating",
    fill_value=0
)
user_similarity=cosine_similarity(user_movie_matrix)

user_similarity_df=pd.DataFrame(
    user_similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)

def collaborative_recommend(user_id, n=10):
    if user_id not in user_similarity_df.index:
        return "user not found"
    similar_users = user_similarity_df[user_id].sort_values(
        ascending=False
    )[1:11]
    similar_users_ids = similar_users.index.tolist()
    watched_movies = set(movielens_df[movielens_df["user_id"]==user_id]["item_id"])
    candidate_movies = movielens_df[
        (movielens_df["user_id"].isin(similar_users_ids)) &
        (movielens_df["rating"]>=4)
    ]
    candidate_movies = candidate_movies[~candidate_movies["item_id"].isin(watched_movies)]
    recommendations = (candidate_movies.groupby("item_id")
                       .size()
                       .sort_values(ascending=False)
                       .head(n)
                       .index)
    return movielens_df[
        movielens_df["item_id"].isin(recommendations)
    ][["item_id","clean_title"]].drop_duplicates()
    
    