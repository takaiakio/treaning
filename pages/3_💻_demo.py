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

df=pd.DataFrame(df)



st.line_chart(data = df,width = 0,height = 0,use_container_width = True)





