import streamlit as st
import pickle

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movie_list = movies["title"].values

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),
                        reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []

    for i in movie_list:
        movie_id = i[0]

        # fetch poster
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


st.header("Movie recommendations")
selected_movie = st.selectbox(label="Movies", options=movie_list,
                              placeholder="Select movie", index=None)

if st.button(label="Recommend", help="Will recommend similar movies",
             type="secondary") and selected_movie != None:
    st.subheader("Recommended movies")
    recommend_movies = recommend(selected_movie)

    index = 0
    for i in recommend_movies:
        index += 1
        st.write(str(index), ". ", i)
