import streamlit as st
st.title("App No.1")

sidebar = st.sidebar
sidebar.title("Barra lateral")
sidebar.write("Elemento 1")

st.header("Información sobre el Conjunto de Datos")
st.header("Descripción de los datos ")
# Agregamos texto a la seccion principal
st.write("""
Este es un simple ejemplo de una app para predecir
¡Esta app predice mis datos!
""")