import streamlit as st
import pandas as pd

link = "https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv"
data = pd.read_csv(link)

#st.dataframe(data)
st.title("Titanic Dataset")
selected = st.selectbox("Select sex",data['sex'].unique())

st.write(f"Selected Option: {selected!r}")
filtered_data = data[data['sex'] == selected]

st.dataframe(filtered_data)