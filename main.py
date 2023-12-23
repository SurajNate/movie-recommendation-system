import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=efecb79104042aa6e502220a90ca7335&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommned(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distences = similarity[movie_index]
    movies_list = sorted(list(enumerate(distences)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommneded_movies = []
    recommneded_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommneded_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommneded_movies_posters.append(fetch_poster(movie_id))
    return recommneded_movies,recommneded_movies_posters



similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')


seleccted_movie_name = st.selectbox(
    'Enter The movie That You Watched and want recommendations on : ',
    movies['title'].values)

if st.button('Recommned'):
    names,posters = recommned(seleccted_movie_name)

    with st.container():
            
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])

    with st.container():
            
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(names[5])
            st.image(posters[5])
        with col2:
            st.text(names[6])
            st.image(posters[6])
        with col3:
            st.text(names[7])
            st.image(posters[7])
        with col4:
            st.text(names[8])
            st.image(posters[8])
        with col5:
            st.text(names[9])
            st.image(posters[9])


hide_stremlit_styles = """
    <style>
    header{visibility:hindden}
    footer{visibility:hindden}
    </style>
"""
st.markdown(hide_stremlit_styles,unsafe_allow_html=True)

st.text('By @suraj_nate')