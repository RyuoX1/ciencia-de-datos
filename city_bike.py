import pandas as pd
import streamlit as st
import matplotlib.pyplot as ptl

link = 'https://raw.githubusercontent.com/adsoftsito/nosql/refs/heads/main/csv/citibike-tripdata.csv'

sidebar = st.sidebar
sidebar.title("City Bikers")
st.title("Cicle Rides in NYC")

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
agreedatos = sidebar.checkbox("Mostrar datos")
if agreedatos:
    st.title("Datos")
    st.dataframe(data)
#-
data['started_at'] = pd.to_datetime(data['started_at'])
data['horas'] = data['started_at'].dt.hour
agreegrafica = sidebar.checkbox("Mostrar grafica")
if agreegrafica:
    fig, ax = ptl.subplots()
    ax.hist(data.horas)
    st.header("Horas")
    st.pyplot(fig)

#-
hora = sidebar.slider(
    "Hora",
    min_value=0,
    max_value=24
)
#-

