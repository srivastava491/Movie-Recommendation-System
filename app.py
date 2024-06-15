import pickle

import pandas as pd
import numpy as np
import streamlit as st

movies=pd.read_csv('movies2.csv')
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index=movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    l=[]
    for i in distances[1:6]:
        l.append(movies.iloc[i[0]].title)
    return l;


movie = st.selectbox(
    "How would you like to be contacted?",
    movies.title.unique())

if st.button("Recommend"):
    for i in recommend(movie):
        st.write(i)
else:
    st.write("Goodbye")