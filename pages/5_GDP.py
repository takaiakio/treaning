import streamlit as st
import plotly.express as px

st.title('一人あたりのGDPと平均寿命、サイズは人口')
df = px.data.gapminder()

country=st.text_input('国を入力', 'Japan')
year=st.number_input('年(1952~5年おき)',1952,2007,1952,step=5)

st.sidebar.title('軸の設定')
xmin=st.sidebar.number_input('x最小値：',0,100,0)
xmax=st.sidebar.number_input('x最大値：',0,10000,4000)
ymin=st.sidebar.number_input('y最小値：',0,100,0)
ymax=st.sidebar.number_input('y最大値：',0,100,100)

df_px=df[df['year'] ==year]
df_country = df[df['country'] ==country]
df_ano=df_country[df_country['year'] ==year]

fig=px.scatter(df_px, x="gdpPercap", y="lifeExp", size="pop", color="continent",hover_name="country",range_x=[xmin,xmax],range_y=[ymin,ymax])

fig.add_annotation(
        x=df_ano.iloc[0,5],
        y=df_ano.iloc[0,3],
        xref="x",
        yref="y",
        text=country,
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
        )

st.plotly_chart(fig, use_container_width=True)