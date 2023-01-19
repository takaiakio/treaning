import streamlit as st
import pandas as pd

#For Excel File
#df = pd.read_excel('world-happiness-report-2021.xlxs')

#For CSV File
#df = pd.read_csv("world-happiness-report-2021.csv")

uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        engine='python',
        na_values='-',
        skipinitialspace=True,
        encoding="shift-jis"
        )

#st.markdown('### アクセスログ（先頭5件）')
#st.write(df.head(5))

st.dataframe(df)





st.title('World Happiness Index 2021:')
st.sidebar.title('World Happiness Index 2021:')

#st.image(
#    'https://images.pexels.com/photos/573259/pexels-photo-573259.jpeg?cs=srgb&dl=pexels-matheus-bertelli-573259.jpg&fm=jpg', 
#     caption='World Happiness Dataset'
#    )


st.image('Company.JPG')

#Country Select Filterunt
country_list = ["All","Western Europe", "South Asia", "Southeast Asia", "East Asia", "North America and ANZ","Middle East and North Africa", "Latin America and Caribbean","Central and Eastern Europe","Commonwealth of Independent States","Sub-Saharan Africa"]
select = st.sidebar.selectbox('Filter the region here:', country_list, key='1')
if select =="All":
   filtered_df = df
else:
   filtered_df = df[df['Regional indicator']==select]
#Ladder Score Slider
score = st.sidebar.slider('Select min Ladder Score', min_value=5, max_value=10, value = 10) # Getting the input.

df = df[df["Area4最"] <= score] # Filtering the dataframe.

#Line Chart
st.line_chart(data=None, width=0, height=0, use_container_width=True)
#Area Chart
st.area_chart(data=None, width=0, height=0, use_container_width=True)



import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
#Scatter Chart
fig = px.scatter(filtered_df,
x="Area1中",
y="Area1最",
size="Ladder score",
color="Regional indicator",
hover_name="Country name",
size_max=10)
st.write(fig)
#Bar Chart, you can write in this way too
st.write(px.bar(filtered_df, y='Ladder score', x='Country name'))
#Seaborn Heatmap
#correlate data
corr = filtered_df.corr()
#using matplotlib to define the size
plt.figure(figsize=(8, 8))
#creating the heatmap with seaborn
fig1 = plt.figure()
ax = sns.heatmap(corr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(20, 220, n=200),
square=True
)
ax.set_xticklabels(
ax.get_xticklabels(),
rotation=45,
horizontalalignment='right'
);
st.pyplot(fig1)