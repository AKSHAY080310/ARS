from recommender.content_model import recommend_similar_movies,recommend_by_user_history
result=recommend_similar_movies("rrr")
#print(result)
print(recommend_by_user_history(user_id=1))