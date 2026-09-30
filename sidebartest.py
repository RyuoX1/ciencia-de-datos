import streamlit as st
import pandas as pd
link = "https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv"
data = pd.read_csv(link)

st.title("Aplicación Web para analizar los datos de WalMart USA.")
#skdhakjsdhakjdhakjdhalksdhlkashdlkahsdkahs
sidebar = st.sidebar
sidebar.title("Barra lateral")
sidebar.write("Elemento 1")

st.header("WalMart")

st.write("""
predicción de ventas de productos de línea blanca en el
noroeste de los Estados Unidos.
""")