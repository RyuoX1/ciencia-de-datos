import streamlit as st
myname = st.text_input('Escribe tu nombre :')
if (myname):
    st.write(f"tu nombre es : {myname}")
