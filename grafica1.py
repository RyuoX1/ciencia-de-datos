import pandas as pd
import streamlit as st
import matplotlib.pyplot as ptl

titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.header("Data Description")
fig, ax = ptl.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)