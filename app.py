import streamlit as st
import pandas as pandas

st.write(
'''
### Largest of three numbers
'''
)

a = st.number_input('Enter a number: ')
b = st.number_input('Enter a number: ')
c = st.number_input('Enter a number: ')

m = max(a,b,c)

st.write(''' 
         The largest of three numbers is:
         ''',)

print('Largest of three numbers are:',m)
