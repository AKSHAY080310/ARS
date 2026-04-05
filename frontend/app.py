import streamlit as st
print("Starting Streamlit app...")

import sys
import os

sys.path.append(os.path.abspath("."))
from backend.auth import add_user, login_user
from backend.ratings import add_rating
from backend.utils import search_movies
from backend.recommend import recommend_movies

st.title("Movie Recommendation System")

if "user_id" not in st.session_state:
    st.session_state.user_id = None
st.sidebar.header("Login / Signup")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Signup"):
    st.sidebar.success(add_user(username, password))

if st.sidebar.button("Login"):
    user_id = login_user(username, password)
    if user_id:
        st.session_state.user_id = user_id
        st.sidebar.success("Logged in!")
    else:
        st.sidebar.error("Invalid credentials")

if st.session_state.user_id:

    st.subheader("Search Movie")

    query = st.text_input("Enter movie name")

    if query:
        results = search_movies(query)

        if results:
            movie_options = {
                f"{title} ({year})": movie_id
                for movie_id, title, year in results
            }

            selected_movie = st.selectbox(
                "Select Movie", list(movie_options.keys())
            )

            rating = st.slider("Rate this movie", 1, 5)

            if st.button("Submit Rating"):
                movie_id = movie_options[selected_movie]
                st.success(add_rating(st.session_state.user_id, movie_id, rating))

    st.subheader("Recommended Movies")

    if st.button("Get Recommendations"):
        recs = recommend_movies(st.session_state.user_id)

        for movie, score in recs.items():
            st.write(f"{movie} {round(score, 2)}")

else:
    st.info("Please login to continue")