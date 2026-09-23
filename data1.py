import streamlit as st
import pandas as pd 

names_link = "https://raw.githubusercontent.com/RyuoX1/Juegos-de-Steam/refs/heads/main/steam_games.csv"
names_data = pd.read_csv(names_link)

st.title("streamlit and pandas")
st.dataframe(names_data)