import pickle
import streamlit as st 
import requests 

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZTkyOGY5Y2IwY2RjMzY2NjIwYjE4N2FkODEzMzhiZiIsIm5iZiI6MTc2MjE4NjA3MS4zODYsInN1YiI6IjY5MDhkMzU3YzlhMDMxOTU1NmRkODkxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.rkq4hUakHobIgYlbnoVNMDS--tR2G1vAe3bROSxtLds"
    }

    data = requests.get(url, headers=headers)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

    
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x: x[1])
    recommended_movies = []
    recommended_movies_poster = []
    for idx in distances[1:6]:
        movie_id = movies.iloc[idx[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[idx[0]].title)

    return recommended_movies, recommended_movies_poster

st.header('Movie Recommendation System')

movies = pickle.load(open('Artifacts\movies.pkl','rb'))
similarity = pickle.load(open('Artifacts\similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie =st.selectbox(
    'Enter or select a movie',
    movie_list,
    index=None,
    placeholder="Select a movie"
)

if st.button('Show Recommendation'):
    recommeded_movies_names, recommeded_movies_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommeded_movies_names[0])
        st.image(recommeded_movies_posters[0])
    with col2:
        st.text(recommeded_movies_names[1])
        st.image(recommeded_movies_posters[1])
    with col3:
        st.text(recommeded_movies_names[2])
        st.image(recommeded_movies_posters[2])
    with col4:
        st.text(recommeded_movies_names[3])
        st.image(recommeded_movies_posters[3])
    with col5:
        st.text(recommeded_movies_names[4])
        st.image(recommeded_movies_posters[4])