import streamlit as st
import pickle
import pandas as pd
import numpy as np


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
#
# from joblib import load
#
# similarity = load('similarity.joblib')

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Recommender")
selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

theme = st.radio("Choose theme", options=["Light", "Dark"])

