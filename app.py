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
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)



    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        })

    option = st.selectbox(
        'Which number do you like best?',
        df['first column']
    )
    st.write('You selected: ', option)