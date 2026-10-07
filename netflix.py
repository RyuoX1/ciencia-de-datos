import pandas as pd
import streamlit as st

link = 'https://raw.githubusercontent.com/RyuoX1/ciencia-de-datos/refs/heads/main/movies.csv'

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
#-
agreefilmes = sidebar.checkbox("Mostrar todos los filmes ")
if agreefilmes:
    st.title("Todos los filmes")
    st.dataframe(data)
#-
filme = sidebar.text_input('Titulo de filme :')
if sidebar.button('Buscar Filmes'):
    filmes = data[data['name'].str.contains(filme, case=False, na=False)]
    st.write("Filmes encontrados ", len(filmes),":")
    st.dataframe(filmes[['gross', 'name', 'rating', 'released', 'runtime', 'genre', 'year']])
#-
director = sidebar.selectbox("Seleccionar Director", data['director'].unique())
if sidebar.button('Filtrar director'):
    directores= data[data['director'] == director]
    st.write("Filmes del director '", director,"' encontrados ", len(directores),":")
    st.dataframe(directores[['budget', 'company', 'country', 'director', 'genre']])

sidebar.write("Equipo 3: ")
sidebar.write("- Victor Emiliano Vasquez Benitez")
sidebar.write("- Elias Martinez Flores")