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

import numpy as np
import pandas as pd

st.title('My first app')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c']
 )
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [35.7, 139.67],
    columns=['lat', 'lon']
)
st.map(map_data)