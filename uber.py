import pandas as pd
import streamlit as st

link = 'https://raw.githubusercontent.com/RyuoX1/ciencia-de-datos/refs/heads/main/uber-raw-data-sep14.csv'
date = 'date/time'

st.title('Uber NYC')
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(link, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date] = pd.to_datetime(data[date])
    return data
data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[date].dt.hour == hour_to_filter]
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
