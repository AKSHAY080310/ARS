import sys
sys.stdout.reconfigure(encoding='utf=-8')
from recommender.cold_start import cold_start_recommend,find_similar_users,get_top_genres,recommend_tmdb_by_genres,fallback_popular
"""users=find_similar_users(25,1,"engineer")
print(users)
print(get_top_genres(users))
print(recommend_tmdb_by_genres(get_top_genres(users),"en"))"""
result=fallback_popular("te")
print(result[["title","genres","score"]])


"""result=cold_start_recommend(25,1,"engineer","en")
print(result[["title","genres","score"]])"""
