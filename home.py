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