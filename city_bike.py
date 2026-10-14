import pandas as pd
import streamlit as st
import matplotlib.pyplot as ptl

link = 'https://raw.githubusercontent.com/adsoftsito/nosql/refs/heads/main/csv/citibike-tripdata.csv'

sidebar = st.sidebar
sidebar.title("City Bikers")
st.title("Cicle Rides in NYC")
#-Funcion carga
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(link, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
#-Cargar x
data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")
#-Convertir a fecha y despues crear campo hora
data['started_at'] = pd.to_datetime(data['started_at'])
data['horas'] = data['started_at'].dt.hour
horas = data['horas'].value_counts().sort_index() #variable con campo hora ordenado por hora

#-sidebar
adatos = sidebar.checkbox("Mostrar datos")
agrafica = sidebar.checkbox("Mostrar grafica")
hora = sidebar.slider(
    "Hora",
    min_value=0,
    max_value=24
)
sidebar.write("Integrantes: Victor Emiliano Vásquez Benítez, Elias Martinez Flores")
#-Tabla
if adatos:
    st.title("Datos")
    st.dataframe(data)

#-Grafoca
if agrafica:
    fig, ax = ptl.subplots()
    ax.bar(x=horas.index, height=horas.values)
    st.title("Horas")
    st.pyplot(fig)
    #st.bar_chart(horas)
#-Mapa
st.title("Mapa")
data.rename({"start_lat": "lat", "start_lng": "lon"}, axis=1, inplace=True) #renombrar latitud y longitud para hacerlos compatibles con map
map_data =data[data["horas"]==hora]
st.map(map_data)
