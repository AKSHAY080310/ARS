import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("."))

from backend.auth import add_user, login_user
from backend.interactions import count_user_interactions, log_interaction
from backend.movie_search import search_movies
from backend.movie_details import get_movie_details
from backend.ratings import add_rating

from recommender.cold_start import cold_start_recommend
from recommender.content_model import recommend_by_user_history
from recommender.hybrid_model import hybrid_recommend


st.set_page_config(page_title="Advanced Movie Recommendation System")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "selected_movie_id" not in st.session_state:
    st.session_state.selected_movie_id = None

st.title("Advanced Movie Recommendation System")

if not st.session_state.logged_in:

    menu = st.sidebar.selectbox("Choose Option", ["Login", "Signup"])

    if menu == "Signup":

        st.subheader("Create Account")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        age = st.number_input("Age", min_value=1, max_value=100)

        gender = st.selectbox("Gender", ["male", "female"])

        occupation = st.text_input("Occupation")

        preferred_language = st.selectbox(
            "Preferred Language",
            ["te", "hi", "ta", "ml", "kn", "en"]
        )

        if st.button("Signup"):

            result = add_user(
                username,
                password,
                age,
                gender,
                occupation,
                preferred_language
            )

            st.success(result)

    elif menu == "Login":

        st.subheader("Login")

        username = st.text_input("Enter Username")
        password = st.text_input("Enter Password", type="password")

        if st.button("Login"):

            user = login_user(username, password)

            if user:

                st.session_state.logged_in = True
                st.session_state.user_id = user["user_id"]
                st.session_state.age = user["age"]
                st.session_state.gender = user["gender"]
                st.session_state.occupation = user["occupation"]
                st.session_state.preferred_language = user["preferred_language"]

                st.rerun()

            else:

                st.error("Invalid Credentials")

else:

    user_id = st.session_state.user_id

    if st.session_state.selected_movie_id is None:

        st.success("Login Successful")
        st.subheader("Recommended For You")

        interaction_count = count_user_interactions(user_id)

        if interaction_count == 0:

            recommendations = cold_start_recommend(
                age=st.session_state.age,
                gender=st.session_state.gender,
                occupation=st.session_state.occupation,
                language=st.session_state.preferred_language
            )

        elif interaction_count < 5:

            recommendations = recommend_by_user_history(user_id)

        else:

            recommendations = hybrid_recommend(user_id)

        for index, row in recommendations.iterrows():

            if st.button(row["title"], key=f"rec_{row['movie_id']}"):

                log_interaction(user_id, row["movie_id"], "click")
                st.session_state.selected_movie_id = row["movie_id"]
                st.rerun()

        st.subheader("Search Movies")

        search_query = st.text_input("Enter Movie Name")

        if search_query:

            search_results = search_movies(search_query)

            for movie in search_results:

                movie_id = movie[0]
                movie_title = movie[1]

                if st.button(movie_title, key=f"search_{movie_id}"):

                    log_interaction(user_id, movie_id, "click")
                    st.session_state.selected_movie_id = movie_id
                    st.rerun()

                if st.button(f"Watchlist {movie_title}", key=f"watch_{movie_id}"):

                    log_interaction(user_id, movie_id, "watchlist")
                    st.success(f"Added {movie_title} to Watchlist")

        if st.button("Logout"):

            st.session_state.logged_in = False
            st.rerun()

    else:

        movie = get_movie_details(st.session_state.selected_movie_id)

        st.subheader(movie["title"])
        st.write("Genres:", movie["genres"])
        st.write("Director:", movie["director"])
        st.write("Cast:", movie["cast_names"])
        st.write("Overview:", movie["overview"])
        st.write("Language:", movie["language"])
        rating = st.slider("Rate this movie", 1, 5, key=f"rate_{movie['movie_id']}")

        if st.button("Submit Rating"):

            add_rating(user_id, movie["movie_id"], rating)
            st.success("Rating submitted!")

        if st.button("Add to Watchlist"):

            log_interaction(user_id, movie["movie_id"], "watchlist")
            st.success("Added to Watchlist!")

        if st.button("Back"):

            st.session_state.selected_movie_id = None
            st.rerun()

