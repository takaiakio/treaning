#import streamlit as st
#import pandas as pd

#For Excel File
#df = pd.read_excel('world-happiness-report-2021.xlxs')

#For CSV File
#df = pd.read_csv("world-happiness-report-2021.csv")

#uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

#if uploaded_file is not None:
#    df = pd.read_csv(
#        uploaded_file,
#        engine='python',
#        na_values='-',
#        skipinitialspace=True,
#        encoding="shift-jis"
#        )

#st.markdown('### アクセスログ（先頭5件）')
#st.write(df.head(5))

#st.dataframe(df)



import streamlit as st
import altair as alt
from vega_datasets import data

st.markdown(
    '''
    StreamlitでAltairのインタラクティブなグラフを表示する方法
    '''
)

# データサンプルを取得
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source

source = get_data()

chart = alt.Chart(source).mark_line().encode(
    x="date:T",
    y="price",
    color="symbol"
)

st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(source).mark_line().encode(
    x="date:T",
    y="price",
    color=alt.Color("symbol", sort=None)
)

st.altair_chart(chart, use_container_width=True)



