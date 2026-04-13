import pandas as pd
import os
tmdb_df=pd.read_pickle(os.path.join("data","processed","tmdb_for_content.pkl"))
movielens_df=pd.read_pickle(os.path.join("data","processed","movielens_for_collaborative.pkl"))
def find_similar_users(age,gender,occupation,top_n=20):
    unique_users=movielens_df[["user_id","age","gender","occupation"]].drop_duplicates()
    unique_users["age_score"]=1-(abs(unique_users["age"]-age)/50)
    unique_users["gender_score"]=(unique_users["gender"]==gender).astype(int)
    unique_users["occupation_score"]=(unique_users["occupation"]==occupation).astype(int)
    unique_users["similarity_score"]=(
        unique_users["age_score"]*0.4 +
        unique_users["gender_score"]*0.3 +
        unique_users["occupation_score"]*0.3
    )
    top_users=unique_users.sort_values(
        by="similarity_score",
        ascending=False
    ).head(top_n)
    return movielens_df[movielens_df["user_id"].isin(top_users["user_id"])]

def get_top_genres(similar_users):
    liked_movies=similar_users[similar_users["rating"]>=4]
    top_genres=(
        liked_movies["genre_label"]
        .value_counts()
        .head(3)
        .index
        .tolist()
    )
    return top_genres

def recommend_tmdb_by_genres(genres,language,n=10):
    filtered=tmdb_df[tmdb_df["language"]==language].copy()
    genre_pattern="|".join(genres)
    filtered=filtered[
        filtered["genres"].str.contains(
            genre_pattern,
            case=False,
            na=False
        )
    ]
    filtered["score"]=(
        filtered["popularity"]*0.5+
        filtered["vote_average"]*0.3+
        filtered["vote_count"]*0.2
    )
    return filtered.sort_values(
        by="score",
        ascending=False
    ).head(n)
    
    
def fallback_popular(language,n=10):
    filtered=tmdb_df[tmdb_df["language"]==language].copy()
    filtered["score"]=(
        filtered["popularity"]*0.5+
        filtered["vote_average"]*0.3+
        filtered["vote_count"]*0.2
    )
    return filtered.sort_values(
        by="score",
        ascending=False
    ).head(n)
    
def cold_start_recommend(age,gender,occupation,language):
    similar_users=find_similar_users(age,gender,occupation)
    if similar_users.empty:
        return fallback_popular(language)
    top_genres=get_top_genres(similar_users)
    if not top_genres:
        return fallback_popular(language)
    recommendations=recommend_tmdb_by_genres(top_genres,language)
    return recommendations    
    