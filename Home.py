import streamlit as st
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

import altair as alt
from vega_datasets import data

source = data.cars()

fig = alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).properties(
    width=500,
    height=500
).interactive()

st.write(fig)


answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')


agree = st.checkbox('I agree')

if agree == True :
     st.write('Great!')