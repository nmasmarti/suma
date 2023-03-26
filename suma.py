import streamlit as st

n1 = st.number_input('Sumand 1')
n2 = st.number_input('Sumand 2')
st.write('El resultat de la suma és: ', n1+n2)