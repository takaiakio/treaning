import streamlit as st
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

import pandas as pd
if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        engine='python',
        na_values='-',
        header=None)

st.markdown('### アクセスログ（先頭5件）')
st.write(df.head(5))

st.title('World Happiness Index 2021:')
st.sidebar.title('World Happiness Index 2021:')
st.image('https://images.pexels.com/photos/573259/pexels-photo-573259.jpeg?cs=srgb&dl=pexels-matheus-bertelli-573259.jpg&fm=jpg', 
         caption='World Happiness Dataset')

#Country Select Filter
country_list = ["All","Western Europe", "South Asia", "Southeast Asia", "East Asia", "North America and ANZ","Middle East and North Africa", "Latin America and Caribbean","Central and Eastern Europe","Commonwealth of Independent States","Sub-Saharan Africa"]
select = st.sidebar.selectbox('Filter the region here:', country_list, key='1')
if select =="All":
   filtered_df = df
else:
   filtered_df = df[df['Regional indicator']==select]
#Ladder Score Slider
score = st.sidebar.slider('Select min Ladder Score', min_value=5, max_value=10, value = 10) # Getting the input.
df = df[df['Ladder score'] <= score] # Filtering the dataframe.

#Line Chart
st.line_chart(data=None, width=0, height=0, use_container_width=True)
#Area Chart
st.area_chart(data=None, width=0, height=0, use_container_width=True)

