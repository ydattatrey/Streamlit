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

animal = ['dog','cat']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'