import streamlit as st

st.title('もう何度目かのStreamlit!')
st.markdown(
    '''
    私はアプリ作成を練習しています!
    '''
)
with st.sidebar:
    st.subheader('News!🆕')
    st.text('画像認識AIが追加されました！')


import plotly.graph_objs as go

animals = ['giraffes', 'orangutans', 'monkeys']
populations = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "Animal",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='Title')

st.plotly_chart(fig, use_container_width=True)

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