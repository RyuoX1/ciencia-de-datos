import streamlit as st
import pandas as pd
import datetime
st.title("App No.1")

sidebar = st.sidebar
sidebar.title("Barra lateral")
sidebar.write("Elemento 1")

st.header("Información sobre el Conjunto de Datos")

st.write("""
Este es un simple ejemplo de una app para predecir
¡Esta app predice mis datos!
""")
titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.header("Datatime")
today = datetime.date.today()
today_date = st.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))

st.header("Dataset")
selected_town = st.radio("Select Embark Town", titanic_data['embark_town'].unique())
st.write("Selected Embark Town:", selected_town)

optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare']) & (titanic_data['embark_town'] == selected_town)]
agree = st.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(subset_fare)
