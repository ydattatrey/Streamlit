import streamlit as st
import pandas as pandas

st.write(
'''
### Largest of three numbers
'''
)

a = st.number_input('Enter first number: ')
b = st.number_input('Enter second number: ')
c = st.number_input('Enter third number: ')

m = max(a,b,c)
print('Largest of three numbers are:',m)
st.write(''' 
         The largest of three numbers is:
         ''')
st.write(m)


