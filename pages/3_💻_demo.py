import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")
import pandas as pd
if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        engine='python',
        na_values='-',
        encoding='shift-jis',
        )

st.dataframe(df)


import numpy as np
import matplotlib.pyplot as plt

# テキストの描画
st.title('Sample page')
st.header('Header')
st.markdown('''
チョコボールの内容量

- ピーナッツ
  - 28g
- いちご
  - 25g
''')

#@st.cache
def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))
    return df
dataframe = rand_df(c=3, r=10)

# 表の描画
st.dataframe(dataframe.head(n=3))
# チャートの描画
st.line_chart(dataframe)
# widget
lst_flavors = ['ピーナッツ', 'いちご']
select_taste = st.selectbox('Flavor', lst_flavors)
# Sidebar
st.sidebar.header('サイドバー')
p = st.sidebar.slider('確率の設定', min_value=0.0, max_value=1.0, value=0.8)
st.sidebar.write(f'設定値は {p} です')



st.line_chart(data = df,width = 0,height = 0,use_container_width = True)





