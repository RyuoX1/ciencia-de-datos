import pandas as pd
import streamlit as st

link = '/workspaces/ciencia-de-datos/movies.csv'

sidebar = st.sidebar
sidebar.title("Netflix")
st.title("Netflix app")

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(link, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

agree = sidebar.checkbox("Mostrar todos los filmes ")

filme = sidebar.text_input('Titulo de filme :')
if sidebar.button('Search'):
    st.write(f"search name : {filme}")
    data = data[data['name'] == filme]
director = sidebar.radio("Seleccionar Director", data['director'].unique())
st.write("Director:", director)

if agree:
    st.title("Todos los filmes")
    st.dataframe(data)