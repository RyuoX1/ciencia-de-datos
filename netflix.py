import pandas as pd
import streamlit as st

link = 'https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv'
data = pd.read_csv(link)
sidebar = st.sidebar
agree = st.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(data)