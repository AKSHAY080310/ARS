import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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
    
    