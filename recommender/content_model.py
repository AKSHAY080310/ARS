import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from backend.interactions import get_interacted_movie_ids
tmdb_df=pd.read_pickle(os.path.join("data","processed","tmdb_for_content.pkl"))
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(tmdb_df["combined_features"])
similarity=cosine_similarity(tfidf_matrix)
def recommend_similar_movies(movie_title,n=10):
    movie_matches= tmdb_df[
        tmdb_df["title"].str.lower() == movie_title.lower()]
    if movie_matches.empty:
        return f"movie '{movie_title}' not found."
    idx=movie_matches.index[0]
    similarity_scores = list(enumerate(similarity[idx]))
    similarity_scores = sorted(similarity_scores,
                               key=lambda x: x[1],
                               reverse=True)
    similarity_scores = similarity_scores[1:n+1]
    movie_indices = [i[0] for i in similarity_scores]
    recommendations=tmdb_df.iloc[movie_indices][["title","genres"]]
    return recommendations

def recommend_by_user_history(user_id,n=10):
    user_movies = get_interacted_movie_ids(user_id)
    if not user_movies:
        return "no interactions found"
    all_recommendations = []
    for movie_id in user_movies:
        movie_match = tmdb_df[tmdb_df["tmdb_id"] == movie_id]
        if movie_match.empty:
            continue
        idx = movie_match.index[0]
        similarity_scores = list(enumerate(similarity[idx]))
        similarity_scores = sorted(similarity_scores,
                                   key = lambda x:x[1],reverse=True)
        similar_movies = similarity_scores[1:n+1]
        for movie in similar_movies:
            all_recommendations.append(movie[0])
            
    movie_counts = Counter(all_recommendations)
    recommend_indices = [
        movie_index
        for movie_index, _ in movie_counts.most_common()
        if tmdb_df.iloc[movie_index]["tmdb_id"] not in user_movies]
    final_indices = recommend_indices[:n]
    return tmdb_df.iloc[final_indices][
        ["tmdb_id","title","genres"]
    ]        
        
    
    